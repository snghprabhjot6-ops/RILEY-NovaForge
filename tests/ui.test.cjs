const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const { JSDOM } = require("jsdom");
const html = fs.readFileSync("riley/static/index.html", "utf8");
const script = fs.readFileSync("riley/static/app.js", "utf8");
const settle = async () => {
  for (let i = 0; i < 5; i++)
    await new Promise((resolve) => setImmediate(resolve));
};

async function app({ fail = false, reply = "The answer is 14." } = {}) {
  const dom = new JSDOM(html, {
    url: "http://127.0.0.1:8765",
    runScripts: "outside-only",
  });
  const w = dom.window;
  const calls = [];
  let chats = [],
    messages = [],
    next = 0;
  w.HTMLDialogElement.prototype.showModal = function () {
    this.setAttribute("open", "");
  };
  w.HTMLDialogElement.prototype.close = function (value = "") {
    this.returnValue = value;
    this.removeAttribute("open");
    this.dispatchEvent(new w.Event("close"));
  };
  w.fetch = async (url, options = {}) => {
    const body = options.body ? JSON.parse(options.body) : null;
    calls.push({ url, body, options });
    let data;
    if (url === "/api/state")
      data = {
        token: "test-token",
        chats,
        language: "en",
        backend: "local",
        model: "llama3.2",
      };
    else if (url === "/api/chats") {
      assert.equal(options.headers["X-Riley-Token"], "test-token");
      const chat = { id: String(++next), title: "New conversation" };
      chats.unshift(chat);
      data = chat;
    } else if (url.startsWith("/api/chats/")) data = { messages };
    else if (url === "/api/chat") {
      if (fail)
        return {
          ok: false,
          json: async () => ({ error: "Ollama is unavailable" }),
        };
      messages = [
        { role: "user", content: body.prompt, language: body.language },
        { role: "assistant", content: reply, language: body.language },
      ];
      chats[0].title = body.prompt;
      data = { messages, chats };
    } else throw new Error(`Unexpected API call ${url}`);
    return { ok: true, json: async () => structuredClone(data) };
  };
  w.eval(script);
  await settle();
  return { w, calls, close: () => dom.window.close() };
}

test("welcome suggestions send a real request and render both turns safely", async () => {
  const a = await app({ reply: "<img src=x onerror=alert(1)> **Hello**" });
  try {
    a.w.document.querySelector('[data-prompt="Hello Riley"]').click();
    await settle();
    assert.equal(
      a.calls.find((c) => c.url === "/api/chat").body.prompt,
      "Hello Riley",
    );
    assert.equal(a.w.document.querySelectorAll(".message").length, 2);
    assert.equal(a.w.document.querySelectorAll(".message img").length, 0);
    assert.match(
      a.w.document.querySelector(".message.assistant").textContent,
      /<img/,
    );
    assert.equal(a.w.document.getElementById("welcome").hidden, true);
    assert.equal(a.w.document.getElementById("prompt").value, "");
    assert.equal(a.w.document.getElementById("export").disabled, false);
  } finally {
    a.close();
  }
});

test("backend failure retains draft, shows the error, and re-enables sending", async () => {
  const a = await app({ fail: true });
  try {
    const p = a.w.document.getElementById("prompt");
    p.value = "Help me plan";
    a.w.document
      .getElementById("composer")
      .dispatchEvent(new a.w.Event("submit", { cancelable: true }));
    await settle();
    assert.equal(p.value, "Help me plan");
    assert.match(
      a.w.document.getElementById("notice").textContent,
      /Ollama is unavailable/,
    );
    assert.equal(a.w.document.getElementById("send").disabled, false);
    assert.equal(a.w.document.querySelectorAll(".message").length, 0);
    assert.equal(a.w.document.getElementById("mic").disabled, true);
  } finally {
    a.close();
  }
});

test("mobile preferences route saves engine, model and response language", async () => {
  const a = await app();
  try {
    const d = a.w.document;
    d.getElementById("mobile-settings").click();
    assert.equal(d.getElementById("settings").open, true);
    d.getElementById("backend").value = "ollama";
    d.getElementById("model").value = "my-model";
    d.getElementById("settings").close("save");
    d.getElementById("language").value = "hi";
    d.getElementById("language").dispatchEvent(new a.w.Event("change"));
    d.getElementById("prompt").value = "नमस्ते";
    d.getElementById("composer").dispatchEvent(
      new a.w.Event("submit", { cancelable: true }),
    );
    await settle();
    const body = a.calls.find((c) => c.url === "/api/chat").body;
    assert.equal(body.backend, "ollama");
    assert.equal(body.model, "my-model");
    assert.equal(body.language, "hi");
    d.getElementById("mobile-theme").click();
    assert.equal(d.documentElement.dataset.theme, "light");
  } finally {
    a.close();
  }
});

test("new chat resets visible messages without deleting earlier conversation", async () => {
  const a = await app();
  try {
    const d = a.w.document;
    d.querySelector('[data-prompt="Hello Riley"]').click();
    await settle();
    d.getElementById("new-chat").click();
    await settle();
    assert.equal(d.querySelectorAll(".message").length, 0);
    assert.equal(d.querySelectorAll(".chat-item").length, 2);
    assert.equal(d.getElementById("welcome").hidden, false);
    assert.equal(a.calls.filter((c) => c.url === "/api/delete").length, 0);
  } finally {
    a.close();
  }
});
