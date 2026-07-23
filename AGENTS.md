---
id: enterprise-ai-coding-engineering/agents-instructions
title: AI Coding Agent 仓库指令
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: technical-lead
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Plan", "Implementation", "Verification", "Review", "Learning"]
applicable_tools: ["Codex", "Claude Code", "Cursor", "Gemini CLI"]
source_type: DECISION
evidence_level: DECISION
risk_level: HIGH
supersedes: null
---

# AI Coding Agent 仓库指令

本文件适用于整个仓库；更深目录可以增加约束，但不得降低本文件和 [治理规则](GOVERNANCE.md) 的标准。

## 工作方式

- 先检查状态、已有内容和适用规则，再做增量修改。
- 使用唯一生命周期，不新建冲突流程。
- 在工作分支或 worktree 修改；保护用户已有和无关变更。
- 普通文档、Schema、模板和校验实现可自主推进。
- 优先确定性命令和可复现 Gate；仅在动态判断有价值时使用 Agent。
- 不以自己的判断作为最终完成证据。

## 边界

未经明确人工批准，不得执行：删除或不可逆操作、远程推送/合并/发布、许可证选择、生产或真实密钥访问、付费/登录外部服务。不得绕过 Policy 或降低校验标准来取得通过结果。

Phase 0–1 禁止批量抓取外部内容、批量生成 Prompt/Skill、复制第三方仓库或实现完整平台。来源未访问时保持 `PENDING_CHECK`，用户说明只能保存为 `user_note`。

## 变更要求

- 受治理 Markdown 使用规定元数据且 ID 唯一。
- Catalog 数据必须通过对应 JSON Schema。
- 正式资产只能位于 `assets/`，Candidate 只能位于 `staging/`。
- 新增本地链接时确保目标存在。
- 失败按治理分类；同类可恢复问题最多重试两次。
- 提交前运行 `python scripts/validate/validate_repository.py` 并自审 Git diff。

## 完成定义

任务只有在验收标准满足、自动校验通过、风险和未决项如实记录、证据可复现时才能标记完成。需要审批的任务停在 `WAITING_APPROVAL`，缺少关键上下文时标记 `BLOCKED`。
