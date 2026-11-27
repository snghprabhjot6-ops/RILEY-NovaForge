# Security Policy

## Supported versions

Riley is in early development and has no published stable release. Security fixes currently apply to the latest commit on the default branch.

## Reporting a vulnerability

Do not include exploit details, credentials, private conversations, or personal data in a public issue.

Use GitHub's private vulnerability-reporting feature when it is available for this repository. If it is not available, contact the repository maintainer through an established private channel and include:

- The affected file or component
- Steps to reproduce the problem
- The potential impact
- A suggested mitigation, if known

Please allow time for investigation before disclosing details publicly. No response-time guarantee is currently offered.

## Credential and data handling

- Never commit `.env`, API keys, passwords, tokens, or private conversation history.
- Use `.env.example` only for non-secret configuration names and safe defaults.
- Treat `.riley/history.json` as private user data.
- Review third-party speech-service privacy terms before changing from the offline speech engine.
- Keep consequential integrations disabled until they have explicit permission checks and tests.
