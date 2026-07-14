# Loop Engineering Co-Builder

> Build agent loops that can prove progress, stop safely, and resume without reconstructing the chat.

[中文](#中文说明) · [English](#english) · [Skill](skills/loop-engineering-co-builder/SKILL.md) · [Design notes](docs/design-notes.md)

![Loop Engineering Co-Builder overview](assets/project-illustrations/01-loop-overview.png)

## 中文说明

`loop-engineering-co-builder` 是一个面向 Codex 的工程化 Skill。它把“让 Agent 一直循环直到完成”改造成一个可检查的控制系统：目标明确、状态可恢复、工具有边界、结果有证据、失败能停止、改进须审批。

它解决的不是“如何让模型多跑几轮”，而是更难也更实际的问题：

- Agent 怎样知道自己真的前进了，而不是反复生成相似内容？
- 中断后，另一个 Agent 怎样从文件状态继续，而不是重读整段聊天？
- 谁来验证结果，避免模型自己宣布自己成功？
- 删除、推送、发布等动作，怎样在循环内部保持人工控制？
- 失败经验怎样转化为改进建议，又不让系统擅自修改自己的规则？

## 核心模型

```text
goal -> observe -> decide -> act -> verify -> persist -> continue | repair | stop
```

项目明确区分两个循环：

1. **任务循环**推进用户目标。
2. **改进循环**根据失败证据提出设计变更，但默认不自动应用。

![Task loop and improvement loop](assets/project-illustrations/02-two-loops.png)

每个项目使用 `.loop/<slug>/` 保存可恢复状态：

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

这七类工件分别回答：做什么、做到哪里、证据是什么、如何接手、哪里失败、怎样改进，以及原始证据在哪里。

## 安装

```bash
git clone https://github.com/2023Anita/loop-engineering-co-builder.git
cp -R loop-engineering-co-builder/skills/loop-engineering-co-builder ~/.codex/skills/
```

重新载入 Codex 后，可显式调用：

```text
Use $loop-engineering-co-builder to turn this goal into a bounded, stateful, verifiable agent loop.
```

也可以直接初始化项目状态：

```bash
python3 ~/.codex/skills/loop-engineering-co-builder/scripts/init_loop.py \
  "Repair one flaky API test" \
  --root "/path/to/project" \
  --slug "repair-flaky-api-test"
```

完成设计后进行结构与状态一致性检查：

```bash
python3 ~/.codex/skills/loop-engineering-co-builder/scripts/validate_loop.py \
  "/path/to/project/.loop/repair-flaky-api-test"
```

## 五种模式

| 模式 | 作用 | 默认边界 |
|---|---|---|
| `design` | 定义目标、状态、验收、权限和停止条件 | 不执行任务 |
| `run` | 执行一个有边界的任务迭代 | 每轮持久化状态 |
| `verify` | 用独立证据检查结果 | 不以自我评价代替验证 |
| `repair` | 诊断失败层并做最小修复 | 不用扩大权限掩盖问题 |
| `improve` | 生成循环设计改进提案 | 默认不自动修改持久规则 |

![Human approval boundary](assets/project-illustrations/03-safety-gate.png)

## 安全边界

- 删除、生产写入、外部发送、正式发布、仓库可见性变更、`git commit` 和 `git push` 默认需要明确授权。
- 状态、日志和证据中只保存密钥名称或引用，不保存密钥值。
- 达到最大迭代次数不等于成功；它应进入 `budget_exhausted`。
- 无法继续时应报告 `blocked` 或 `failed`，而不是伪造“已完成”。
- 改进循环不能自行改写 Skill、`AGENTS.md`、权限或长期记忆。

![Stateful recovery and handoff](assets/project-illustrations/04-recovery-handoff.png)

## 适合与不适合

适合重复性、长时间、可观测、可验证，并且需要恢复或重试的任务，例如代码修复、证据研究、内容生产和发布前验证。

不适合单步回答、没有有效反馈信号的开放式探索，或重试本身会显著放大风险的操作。

## 来源说明

本项目受到 Anthropic 技术演讲及其公开 Loop Engineering 材料启发，并将核心概念重构为适配 Codex 的供应商中立模型。用户提供的原始双语字幕没有进入仓库；仓库只包含重新组织和独立表述的工程原则。

## English

Loop Engineering Co-Builder is a Codex skill for designing bounded, stateful, verifiable, and recoverable agent loops. It separates task execution from self-improvement, requires evidence-backed completion, persists restartable state, and keeps risky actions behind human approval gates.

The core abstraction is:

```text
goal + state + tools + permissions + verification + stop conditions + handoff
```

See the [Skill instructions](skills/loop-engineering-co-builder/SKILL.md) and [design notes](docs/design-notes.md) for the full contract.

## License

[MIT](LICENSE)
