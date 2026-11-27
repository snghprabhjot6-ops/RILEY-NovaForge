# Contributing

Thank you for helping Riley grow.

## Before changing code

1. Open an issue describing the bug or proposal.
2. Check `docs/PROJECT_STATUS.md` so new documentation does not overstate current capability.
3. Keep existing source and branch history intact unless a change explicitly requires migration.

## Development workflow

1. Create and activate a Python virtual environment.
2. Install `requirements.txt`.
3. Make a focused change.
4. Add or update automated tests.
5. Run `python -m pytest`.
6. Update the changelog and status documentation when behavior changes.

## Code expectations

- Keep conversation providers behind the backend interface.
- Avoid shell execution with user-provided input.
- Validate environment settings and fail with a clear message.
- Never commit secrets, credentials, local history, recordings, or user data.
- Keep macOS behavior working and avoid platform assumptions in shared modules.
- Mark unverified Windows behavior honestly.
- Distinguish implemented, tested, environment-dependent, and planned features.

Licensing and external contribution terms have not been declared. Discuss substantial contributions with the maintainer before investing significant work.

For graphical UI changes, run `npm ci --ignore-scripts`, `npm run check`, and `npm test` with Node.js 18+. These DOM tests complement API tests; they do not replace visual or physical audio checks. Keep frontend assets self-contained and escape model content by rendering it as text.
