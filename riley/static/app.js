"use strict";
const $ = (id) => document.getElementById(id);
const SVG_NS = "http://www.w3.org/2000/svg";
const locales = {
  en: "en-US",
  hi: "hi-IN",
  fr: "fr-FR",
  es: "es-ES",
  bn: "bn-BD",
  sa: "sa-IN",
};

const ICON_PATHS = {
  chat: [
    "M3 4.25A1.75 1.75 0 0 1 4.75 2.5h6.5A1.75 1.75 0 0 1 13 4.25v5.5a1.75 1.75 0 0 1-1.75 1.75H6.5L3.5 13.75V11.5A1.75 1.75 0 0 1 3 10.25Z",
  ],
  copy: [
    "M5.5 5.5v-2a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-2",
    "M3.5 5.5h6a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-6a1 1 0 0 1-1-1v-6a1 1 0 0 1 1-1Z",
  ],
  check: ["M3.5 8.5 6.5 11.5 12.5 4.75"],
  volume: [
    "M3 6.5h2.5L9 3.5v9L5.5 9.5H3a.75.75 0 0 1-.75-.75v-1.5A.75.75 0 0 1 3 6.5Z",
    "M11.5 5.75a3.25 3.25 0 0 1 0 4.5",
  ],
};

function createSvgIcon(name) {
  const svg = document.createElementNS(SVG_NS, "svg");
  svg.setAttribute("viewBox", "0 0 16 16");
  svg.setAttribute("fill", "none");
  svg.setAttribute("stroke", "currentColor");
  svg.setAttribute("stroke-width", "1.5");
  svg.setAttribute("stroke-linecap", "round");
  svg.setAttribute("stroke-linejoin", "round");
  for (const d of ICON_PATHS[name] || []) {
    const path = document.createElementNS(SVG_NS, "path");
    path.setAttribute("d", d);
    svg.append(path);
  }
  return svg;
}

function createAstryxButton({
  label,
  variant = "ghost",
  size = "sm",
  icon = null,
  fullWidth = false,
  className = "",
  title = "",
  ariaLabel = "",
} = {}) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = className ? `astryx-button ${className}` : "astryx-button";
  button.dataset.astryxComponent = "button";
  button.dataset.variant = variant;
  button.dataset.size = size;
  if (fullWidth) button.dataset.width = "full";
  if (title) button.title = title;
  if (ariaLabel) button.setAttribute("aria-label", ariaLabel);

  const content = document.createElement("span");
  content.className = "astryx-button-content";

  if (icon) {
    const iconSlot = document.createElement("span");
    iconSlot.className = "astryx-button-icon";
    iconSlot.setAttribute("aria-hidden", "true");
    iconSlot.append(createSvgIcon(icon));
    content.append(iconSlot);
  }

  const labelEl = document.createElement("span");
  labelEl.className = "astryx-button-label";
  labelEl.textContent = label;
  content.append(labelEl);

  button.append(content);
  return { button, labelEl };
}

function setButtonLabel(button, text) {
  const label = button.querySelector(".astryx-button-label");
  if (label) {
    label.textContent = text;
  } else {
    button.textContent = text;
  }
}

let token = "",
  chats = [],
  active = null,
  messages = [],
  busy = false,
  recognition = null,
  voiceOn = false;

let prefs = {};
try {
  prefs = JSON.parse(localStorage.getItem("riley.preferences") || "{}");
} catch {
  /* Storage may be disabled. */
}
if (!prefs || typeof prefs !== "object" || Array.isArray(prefs)) prefs = {};
document.documentElement.dataset.theme =
  prefs.theme === "light" ? "light" : "dark";

function savePrefs() {
  try {
    localStorage.setItem("riley.preferences", JSON.stringify(prefs));
  } catch {
    /* The session still works. */
  }
}

function notice(text = "") {
  $("notice").textContent = text;
  $("notice").hidden = !text;
}

async function api(path, body) {
  const options =
    body === undefined
      ? {}
      : {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Riley-Token": token,
          },
          body: JSON.stringify(body),
        };
  let response;
  try {
    response = await fetch(path, options);
  } catch {
    throw new Error(
      "Riley is disconnected. Check that the launcher window is still open, then reload.",
    );
  }
  let data = {};
  try {
    data = await response.json();
  } catch {
    data = {};
  }
  if (!response.ok)
    throw new Error(data.error || "Something went wrong. Please try again.");
  return data;
}

function modeLabel() {
  const engine = prefs.backend || "local";
  $("mode-label").textContent =
    engine === "ollama"
      ? `Ollama · ${prefs.model || "llama3.2"}`
      : engine === "echo"
        ? "Echo · testing"
        : "Built-in · offline";
  $("capability-note").textContent =
    engine === "ollama"
      ? "Local AI can make mistakes. Verify important details."
      : engine === "echo"
        ? "Echo mode repeats your message for testing."
        : "Built-in mode handles greetings, time, date, and arithmetic.";
}

function renderChats() {
  $("chat-list").replaceChildren();
  if (!chats.length) {
    const p = document.createElement("p");
    p.className = "empty-list";
    p.textContent = "Your conversations will appear here.";
    $("chat-list").append(p);
  }
  for (const c of chats) {
    const isSelected = c.id === active;
    const { button } = createAstryxButton({
      label: c.title,
      variant: "ghost",
      size: "md",
      icon: "chat",
      fullWidth: true,
      className: isSelected ? "chat-item active" : "chat-item",
      title: c.title,
      ariaLabel: `Open conversation: ${c.title}`,
    });
    button.disabled = busy;
    if (isSelected) {
      button.dataset.selected = "true";
      button.setAttribute("aria-current", "true");
    }
    button.addEventListener("click", () => openChat(c.id));
    $("chat-list").append(button);
  }
  $("delete").disabled = busy || !active;
  $("export").disabled = busy || !messages.length;
}

function readAloud(text, language) {
  if (!("speechSynthesis" in window)) {
    notice("Speech output is not available in this browser.");
    return;
  }
  speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = locales[language] || "en-US";
  const voices = speechSynthesis.getVoices();
  const selected = voices.find(
    (v) => v.voiceURI === prefs.voice && v.lang.split("-")[0] === language,
  );
  const matching = voices.filter((v) => v.lang.split("-")[0] === language);
  utterance.voice =
    selected ||
    matching.find((v) =>
      /samantha|zira|jenny|female|woman|heera|swara|denise|helena/i.test(
        v.name,
      ),
    ) ||
    matching[0] ||
    null;
  utterance.onerror = (event) => {
    if (!["interrupted", "canceled"].includes(event.error))
      notice(
        "This voice could not speak. Choose another installed voice in Preferences.",
      );
  };
  speechSynthesis.speak(utterance);
}

async function copyText(text) {
  if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
    await navigator.clipboard.writeText(text);
    return;
  }
  const helper = document.createElement("textarea");
  helper.value = text;
  helper.setAttribute("readonly", "");
  helper.style.position = "fixed";
  helper.style.opacity = "0";
  document.body.append(helper);
  helper.select();
  const ok = document.execCommand && document.execCommand("copy");
  helper.remove();
  if (!ok) throw new Error("Copy unavailable");
}

function renderMessages() {
  $("welcome").hidden = messages.length > 0;
  $("messages").hidden = !messages.length;
  $("messages").replaceChildren();
  for (const m of messages) {
    const row = document.createElement("article");
    row.className = `message ${m.role}`;
    const avatar = document.createElement("div");
    avatar.className = "message-avatar";
    avatar.textContent = m.role === "user" ? "Y" : "R";
    avatar.setAttribute("aria-hidden", "true");
    const body = document.createElement("div");
    body.className = "message-body";
    const heading = document.createElement("div");
    heading.className = "message-heading";
    heading.textContent = m.role === "user" ? "You" : "Riley";
    const time = document.createElement("small");
    const date = new Date(m.created_at);
    time.textContent = Number.isNaN(date.getTime())
      ? ""
      : date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    heading.append(time);
    const content = document.createElement("div");
    content.className = "message-text";
    content.textContent = m.content;
    const actions = document.createElement("div");
    actions.className = "message-actions";

    const { button: copy, labelEl: copyLabel } = createAstryxButton({
      label: "Copy",
      variant: "ghost",
      size: "sm",
      icon: "copy",
      className: "message-action",
    });
    let resetTimer = null;
    copy.addEventListener("click", async () => {
      try {
        await copyText(m.content);
        copyLabel.textContent = "Copied";
        const iconSlot = copy.querySelector(".astryx-button-icon");
        if (iconSlot) iconSlot.replaceChildren(createSvgIcon("check"));
        clearTimeout(resetTimer);
        resetTimer = setTimeout(() => {
          copyLabel.textContent = "Copy";
          if (iconSlot) iconSlot.replaceChildren(createSvgIcon("copy"));
        }, 1800);
      } catch {
        notice("Copy is unavailable. You can select the message text instead.");
      }
    });
    actions.append(copy);

    if (m.role === "assistant") {
      const { button: speak } = createAstryxButton({
        label: "Read aloud",
        variant: "ghost",
        size: "sm",
        icon: "volume",
        className: "message-action",
      });
      speak.addEventListener("click", () => readAloud(m.content, m.language));
      actions.append(speak);
    }

    body.append(heading, content, actions);
    row.append(avatar, body);
    $("messages").append(row);
  }
  $("conversation").scrollTop = $("conversation").scrollHeight;
}

function setBusy(value) {
  busy = value;
  $("prompt").disabled = value;
  $("busy").hidden = !value;
  $("send").setAttribute("aria-busy", String(value));
  for (const id of [
    "send",
    "new-chat",
    "language",
    "settings-open",
    "mobile-settings",
    "mic",
  ]) {
    const el = $(id);
    if (el) el.disabled = value || (id === "mic" && !SpeechRecognition);
  }
  for (const b of document.querySelectorAll("[data-prompt]"))
    b.disabled = value;
  renderChats();
}

async function openChat(id) {
  if (busy) return;
  setBusy(true);
  notice();
  try {
    const data = await api(`/api/chats/${encodeURIComponent(id)}`);
    active = id;
    messages = Array.isArray(data.messages) ? data.messages : [];
    renderMessages();
  } catch (error) {
    notice(error.message);
  } finally {
    setBusy(false);
  }
}

async function newChat() {
  if (busy) return;
  setBusy(true);
  notice();
  try {
    const chat = await api("/api/chats", {});
    chats.unshift(chat);
    active = chat.id;
    messages = [];
    renderMessages();
    $("prompt").value = "";
    $("prompt").style.height = "";
  } catch (error) {
    notice(error.message);
  } finally {
    setBusy(false);
    $("prompt").focus();
  }
}

async function send(event) {
  event.preventDefault();
  const prompt = $("prompt").value.trim();
  if (!prompt || busy) return;
  if (recognition) recognition.stop();
  notice();
  setBusy(true);
  try {
    if (!active) {
      const chat = await api("/api/chats", {});
      chats.unshift(chat);
      active = chat.id;
    }
    const data = await api("/api/chat", {
      chat_id: active,
      prompt,
      language: $("language").value,
      backend: prefs.backend || "local",
      model: prefs.model || "llama3.2",
    });
    const turnMessages = Array.isArray(data.messages) ? data.messages : [];
    messages.push(...turnMessages);
    if (Array.isArray(data.chats)) chats = data.chats;
    $("prompt").value = "";
    $("prompt").style.height = "";
    renderMessages();
    const reply = [...turnMessages].reverse().find((m) => m.role === "assistant");
    if (voiceOn && reply) readAloud(reply.content, $("language").value);
  } catch (error) {
    notice(error.message);
  } finally {
    setBusy(false);
    $("prompt").focus();
  }
}

$("composer").addEventListener("submit", send);
$("prompt").addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey && !event.isComposing) {
    event.preventDefault();
    $("composer").requestSubmit();
  }
});
$("prompt").addEventListener("input", () => {
  $("prompt").style.height = "auto";
  $("prompt").style.height = Math.min($("prompt").scrollHeight, 180) + "px";
});
$("new-chat").addEventListener("click", newChat);

document.addEventListener("keydown", (event) => {
  const activeEl = document.activeElement;
  const activeTag = activeEl ? activeEl.tagName : "";
  if (
    event.key.toLowerCase() === "n" &&
    !event.ctrlKey &&
    !event.metaKey &&
    !event.altKey &&
    !(activeEl && activeEl.isContentEditable) &&
    !["INPUT", "TEXTAREA", "SELECT", "BUTTON"].includes(activeTag) &&
    !document.querySelector("dialog[open]")
  ) {
    event.preventDefault();
    newChat();
  }
});

for (const button of document.querySelectorAll("[data-prompt]")) {
  button.addEventListener("click", () => {
    $("prompt").value = button.dataset.prompt;
    $("composer").requestSubmit();
  });
}

$("language").addEventListener("change", () => {
  prefs.language = $("language").value;
  savePrefs();
  if ("speechSynthesis" in window) speechSynthesis.cancel();
});

$("theme").addEventListener("click", () => {
  prefs.theme =
    document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  document.documentElement.dataset.theme = prefs.theme;
  savePrefs();
});

$("mobile-settings").addEventListener("click", () =>
  $("settings-open").click(),
);
$("mobile-theme").addEventListener("click", () => $("theme").click());

$("voice").addEventListener("click", () => {
  voiceOn = !voiceOn;
  $("voice").setAttribute("aria-pressed", String(voiceOn));
  $("voice").dataset.isPressed = String(voiceOn);
  setButtonLabel($("voice"), voiceOn ? "Voice on" : "Voice off");
  if (!voiceOn && "speechSynthesis" in window) speechSynthesis.cancel();
});

function populateVoices() {
  if (!("speechSynthesis" in window)) return;
  const select = $("voice-select");
  select.replaceChildren(new Option("Automatic · default system voice", ""));
  for (const v of speechSynthesis.getVoices())
    select.add(new Option(`${v.name} · ${v.lang}`, v.voiceURI));
  select.value = prefs.voice || "";
}

if ("speechSynthesis" in window) {
  speechSynthesis.addEventListener("voiceschanged", populateVoices);
  populateVoices();
}

for (const dialogId of ["settings", "confirm-delete"]) {
  const dialog = $(dialogId);
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close("cancel");
  });
}

$("settings-open").addEventListener("click", () => {
  $("backend").value = prefs.backend || "local";
  $("model").value = prefs.model || "llama3.2";
  populateVoices();
  $("settings").returnValue = "";
  $("settings").showModal();
});

$("settings").addEventListener("close", () => {
  if ($("settings").returnValue === "save") {
    prefs.backend = $("backend").value;
    prefs.model = $("model").value.trim() || "llama3.2";
    prefs.voice = $("voice-select").value;
    savePrefs();
    modeLabel();
    notice("Preferences saved. They apply to your next message.");
  }
});

$("export").addEventListener("click", () => {
  if (!messages.length) return;
  const blob = new Blob(
    [
      JSON.stringify(
        {
          app: "RILEY by NovaForge",
          title: chats.find((c) => c.id === active)?.title,
          messages,
        },
        null,
        2,
      ),
    ],
    { type: "application/json" },
  );
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `riley-conversation-${active || "export"}.json`;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});

$("delete").addEventListener("click", () => {
  if (active && !busy) {
    $("confirm-delete").returnValue = "";
    $("confirm-delete").showModal();
  }
});

$("confirm-delete").addEventListener("close", async () => {
  if ($("confirm-delete").returnValue !== "delete" || !active || busy) return;
  setBusy(true);
  try {
    await api("/api/delete", { chat_id: active });
    chats = chats.filter((c) => c.id !== active);
    active = null;
    messages = [];
    renderMessages();
    notice("Conversation deleted.");
  } catch (error) {
    notice(error.message);
  } finally {
    setBusy(false);
  }
});

const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
if (!SpeechRecognition) {
  $("mic").disabled = true;
  $("mic").title =
    "Dictation needs a browser with speech recognition, such as Microsoft Edge or Chrome.";
}

$("mic").addEventListener("click", () => {
  if (!SpeechRecognition) return;
  if (recognition) {
    recognition.stop();
    return;
  }
  if (
    !window.confirm(
      "Start browser dictation? Your browser will request microphone access and may send audio to its speech recognition service.",
    )
  )
    return;
  const session = new SpeechRecognition();
  recognition = session;
  session.lang = locales[$("language").value];
  session.interimResults = false;
  session.maxAlternatives = 1;
  session.onstart = () => {
    $("mic").setAttribute("aria-pressed", "true");
    $("mic").dataset.isPressed = "true";
    setButtonLabel($("mic"), "Listening…");
    notice("Listening. Speak your message; you can review it before sending.");
  };
  session.onresult = (event) => {
    const transcript = event.results?.[0]?.[0]?.transcript || "";
    $("prompt").value = ($("prompt").value + " " + transcript).trim();
    $("prompt").dispatchEvent(new Event("input"));
    notice("Dictation added. Review your message, then send.");
  };
  session.onerror = (event) =>
    notice(
      `Dictation could not finish (${event.error}). Check microphone permissions or type your message.`,
    );
  session.onend = () => {
    recognition = null;
    $("mic").setAttribute("aria-pressed", "false");
    $("mic").dataset.isPressed = "false";
    setButtonLabel($("mic"), "Voice input");
  };
  try {
    session.start();
  } catch {
    recognition = null;
    $("mic").setAttribute("aria-pressed", "false");
    $("mic").dataset.isPressed = "false";
    setButtonLabel($("mic"), "Voice input");
    notice("Could not start the microphone. Try again or type a message.");
  }
});

async function init() {
  setBusy(true);
  try {
    const state = await api("/api/state");
    token = state.token;
    chats = Array.isArray(state.chats) ? state.chats : [];
    prefs.backend = prefs.backend || state.backend;
    prefs.model = prefs.model || state.model;
    $("language").value = locales[prefs.language]
      ? prefs.language
      : state.language;
    modeLabel();
    if (chats.length) {
      active = chats[0].id;
      const chatData = await api(`/api/chats/${encodeURIComponent(active)}`);
      messages = Array.isArray(chatData.messages) ? chatData.messages : [];
    }
    renderMessages();
  } catch (error) {
    notice(error.message);
  } finally {
    setBusy(false);
    if (!SpeechRecognition) $("mic").disabled = true;
    $("prompt").focus();
  }
}

init();
