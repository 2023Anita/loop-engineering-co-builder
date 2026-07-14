# Permission and safety

## Three permission classes

### Allowed

Read-only inspection, local calculation, validation, and reversible project-local edits explicitly inside scope.

### Approval required

Deletion, bulk rewrite, production writes, external messages, publication, repository visibility changes, credential or permission changes, purchases, `git commit`, and `git push`. Existing approval is valid only for the exact action and scope the user authorized.

### Denied

Actions outside scope, secret exfiltration, bypassing controls, silently weakening privacy or safety settings, and modifying durable instructions to make the current loop easier.

## Phase-specific envelopes

Use different capabilities by phase:

- design: read and write loop artifacts only;
- run: task-specific tools only;
- verify: read-only checks plus test execution;
- repair: narrowly scoped edits based on a diagnosed failure;
- improve: proposal writing only until approved.

## Secret handling

- Store references to secret names, never values.
- Do not include credentials in prompts, state, evidence, logs, screenshots, or Git history.
- Redact tool output before persisting it.
- Stop if a task requires a secret through an untrusted channel.

## High-stakes domains

For medical, legal, financial, security, or personally identifiable data, use stricter source verification, sandboxing, audit records, and human review. A loop may assist analysis; it does not replace accountable professional judgment.
