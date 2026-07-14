# Design notes

## Why this is a Skill, not an agent framework

The project owns the design contract around an agent loop: state, permissions, verification, stop logic, recovery, and improvement proposals. It intentionally does not implement a new model client, scheduler, sandbox, or multi-agent runtime.

This boundary keeps the Skill portable. Codex, another agent runtime, CI, or a human operator may execute the actions while the loop artifacts preserve the same engineering contract.

## Why task and improvement loops are separate

A task loop optimizes for reaching the current goal. An improvement loop changes the mechanism used to reach future goals. Combining them creates a governance problem: a blocked task could weaken its own permissions, replace its verifier, or rewrite permanent instructions.

The improvement loop therefore produces a proposal with evidence, risk, rollback, and approval status. Application is a separate authorized action.

## Why completion is evidence-gated

Language models are strong generators and imperfect judges of their own output. A completion claim is therefore treated as state derived from verification, not as prose. The validator checks structural consistency, while each project supplies domain-specific tests or review evidence.

## Why state lives in files

Project-local files are inspectable, versionable, and runtime-neutral. They allow a new agent or human to resume work without relying on hidden conversational state. The state file stays compact; detailed evidence remains in `evidence/`.

## Non-goals

- autonomous privilege expansion;
- unbounded background execution;
- silent modification of durable instructions or memory;
- replacing domain-specific test suites;
- claiming command-level equivalence between Codex and other providers.
