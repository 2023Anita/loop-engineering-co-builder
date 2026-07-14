# Provider adapters

The core loop is provider-neutral. Translate capabilities at the boundary.

| Loop concept | Codex-style implementation | Other agent runtimes |
|---|---|---|
| durable project rules | `AGENTS.md`, Skill instructions | project rules or system context |
| reusable workflow | `SKILL.md` | skills, commands, or workflow definitions |
| tool execution | tool calls and local commands | function or tool calls |
| persistent state | project files under `.loop/` | database, artifact store, or files |
| isolation | sandbox or workspace scope | container, VM, or policy boundary |
| parallel work | subagents or dynamic workflow | agents, jobs, or worker pool |
| deterministic guard | validator, test, permission gate | hook, policy engine, CI, or test |

Do not claim command-level equivalence between providers. Preserve the contract—goal, state, evidence, permissions, and stop logic—while adapting execution details.

Keep provider-specific details out of `state.json` unless they are required to resume. Prefer adapter notes in `loop-spec.md`.
