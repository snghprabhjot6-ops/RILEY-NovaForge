# Security and privacy

Riley is a single-user app for a trusted computer. The graphical server binds only to `127.0.0.1`, checks exact Host and request Origin, and requires a random per-launch token for writes. It serves a fixed list of assets, renders chat content as plain text, and includes a restrictive Content Security Policy. Do not publish it through a reverse proxy or port forward; it does not provide account authentication, TLS or tenant isolation.

The built-in backend does not contact an AI service. Ollama mode sends recent chat context to the configured loopback HTTP endpoint, with proxies and redirects disabled. Browser dictation may transmit microphone audio to the browser vendor's recognition service; the user opts in and reviews the draft before sending. Optional CLI Google recognition also uses a network service.

Chats and exports can contain personal information. The web app stores plaintext SQLite data on the computer, while the CLI stores separate JSON history. Files use restrictive permissions where the OS supports them; this is not encryption or protection from another app running under the same account. Browser preferences do not contain conversation text. Runtime data and `.env` files are ignored by Git.

Never commit credentials, conversation databases or private exports. Riley does not need an API key for its supplied backends. No shell commands or arbitrary file access are exposed to models. Arithmetic uses a constrained syntax tree rather than `eval`.

Report suspected vulnerabilities privately to the repository owner through an available private GitHub reporting channel. Do not include real secrets, private conversations or exploit details in public issues. Dependency and packaging checks should be reviewed before distributing a build. The Windows binary build is unsigned.
