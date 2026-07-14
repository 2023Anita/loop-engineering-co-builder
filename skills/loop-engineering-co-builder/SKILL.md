---
name: loop-engineering-co-builder
description: Design, initialize, run, verify, recover, and improve bounded agent loops. Use when a user wants to turn a repeatable goal into a Loop Engineering project with explicit state, tools, permissions, evidence, stop conditions, handoff, and human approval gates; when an existing agent workflow stalls, drifts, cannot resume, or declares completion without proof; or when adapting Anthropic-style loop ideas into Codex-compatible project artifacts. Do not use for a one-step answer that needs no persistent state or iteration.
---

# Loop Engineering Co-Builder

Build a loop that can answer six questions at any moment: What is the goal? What is the current state? What may act? What proves progress? When must it stop? How can another agent resume it?

## Core contract

Treat a loop as an engineered control system, not a repeated prompt:

`goal -> observe -> decide -> act -> verify -> persist -> continue | repair | stop`

Maintain two separate loops:

1. **Task loop** — advances the user's concrete task.
2. **Improvement loop** — records failure patterns and proposes changes to the loop design.

Never let the improvement loop silently edit this Skill, `AGENTS.md`, permissions, persistent memory, or production configuration. Write an improvement proposal and obtain explicit approval first.

## Decide whether a loop is justified

Use a loop when the task is repeatable or long-running, has observable intermediate state, has a meaningful verifier, and benefits from retry or resumption.

Use a direct workflow instead when the task is a single bounded action, has no useful feedback signal, or would make retries more dangerous than helpful.

If the task is underspecified, resolve only the decisions that materially change scope, risk, or acceptance criteria. For deep requirement discovery, hand off to `$harness-interview-workflow` when available.

## Choose a mode

- `design`: create or revise the loop contract without executing the task.
- `run`: execute one bounded iteration and persist the result.
- `verify`: independently test the current output against acceptance criteria.
- `repair`: diagnose a failed or stalled loop, then make the smallest justified correction.
- `improve`: create a reviewable proposal for changing the loop itself.

Default to `design` for a new loop. Do not move to `run` if required permissions, inputs, acceptance criteria, or stop conditions remain unresolved.

## Build the loop

### 1. Define the contract

Write:

- one concrete goal;
- explicit in-scope and out-of-scope boundaries;
- inputs and expected outputs;
- observable acceptance criteria;
- a finite iteration or resource budget;
- success, failure, stalled, blocked, and budget-exhausted stop conditions.

Read [references/loop-spec-schema.md](references/loop-spec-schema.md) for the required contract.

### 2. Model state before action

Persist machine-readable state under `.loop/<slug>/state.json`. The state must be sufficient for a different agent to resume without reconstructing the full chat.

Allowed statuses are `designed`, `ready`, `running`, `verifying`, `repairing`, `blocked`, `failed`, `completed`, and `budget_exhausted`.

Read [references/state-and-handoff.md](references/state-and-handoff.md) before designing recovery or resume behavior.

### 3. Bound tools and permissions

List allowed, approval-required, and denied actions. Apply least privilege per phase, not one blanket permission set for the entire loop.

Require explicit confirmation immediately before destructive file operations, production writes, publication, message sending, credential changes, repository visibility changes, `git commit`, or `git push`, unless the user already authorized that exact action and scope in the current request.

Read [references/permission-and-safety.md](references/permission-and-safety.md) for safety gates and secret handling.

### 4. Design independent feedback

For every acceptance criterion, define a verifier, its evidence, and its failure signal. Prefer deterministic checks: tests, builds, schemas, linters, parsers, screenshots, API reads, repository state, or human review.

The same model saying “looks correct” is not independent evidence. Read [references/verification-patterns.md](references/verification-patterns.md).

### 5. Initialize artifacts

Run:

```bash
python3 scripts/init_loop.py "<goal>" --root "<project-root>" --slug "<loop-slug>"
```

This creates:

```text
.loop/<slug>/
├── loop-spec.md
├── state.json
├── verification-report.md
├── handoff.md
├── retrospective.md
├── improvement-proposal.md
└── evidence/
```

Edit the generated placeholders before execution. Never treat the scaffold as an approved plan.

### 6. Execute bounded iterations

For each iteration:

1. Read `loop-spec.md` and `state.json`.
2. Confirm status, budget, dependencies, and approval gates.
3. Select one smallest action that advances a criterion.
4. Execute only that bounded action.
5. Capture evidence and verifier output.
6. Update `state.json` atomically in meaning: iteration, status, completed work, next action, evidence, and blocker.
7. Stop, repair, or continue according to the contract.

For broad multi-agent orchestration, delegate execution mechanics to `$codex-dynamic-workflows` when available. This Skill retains ownership of the loop contract, state model, verification policy, and stop logic.

### 7. Verify before completion

Run:

```bash
python3 scripts/validate_loop.py "<project-root>/.loop/<slug>"
```

Then execute the domain-specific verifiers in `loop-spec.md`. Mark `completed` only when every required criterion passes and `verification-report.md` records `Overall status: PASS` with evidence.

### 8. Handoff and improve

On stop, write `handoff.md` with current state, evidence, exact next action, and unresolved approvals. Write `retrospective.md` only from observed behavior.

If a durable improvement is justified, use `improve` mode and write `improvement-proposal.md` with evidence, proposed change, expected benefit, risk, rollback, and approval status. Do not apply it automatically.

## Repair logic

Classify the failure before changing the loop:

- `goal_error`: acceptance target is ambiguous or contradictory;
- `state_error`: state is missing, stale, or not resumable;
- `tool_error`: capability, environment, or dependency failed;
- `permission_error`: action is not authorized;
- `verification_error`: verifier is absent, circular, flaky, or misleading;
- `strategy_error`: repeated action does not reduce distance to the goal;
- `budget_error`: remaining budget cannot support another meaningful iteration.

Change one layer at a time. Preserve evidence from failed attempts. Read [references/failure-patterns.md](references/failure-patterns.md) before increasing retries or permissions.

## Provider boundary

Keep the loop specification provider-neutral. Map tools, sandboxing, skills, agents, and permission mechanisms through a provider adapter rather than copying vendor-specific commands into the core model. Read [references/provider-adapters.md](references/provider-adapters.md).

## Examples and provenance

- Read [references/examples.md](references/examples.md) for article, code repair, research, and safety-blocked loops.
- Read [references/core-loop-model.md](references/core-loop-model.md) for the conceptual model.
- Read [references/anthropic-loop-engineering.md](references/anthropic-loop-engineering.md) for source provenance and carefully bounded claims.

## Completion rule

A loop is not complete because it reached an iteration limit, produced a plausible artifact, or exhausted context. Completion requires passing evidence, persisted state, and a usable handoff. If any is missing, report the truthful terminal state instead.
