---
id: enterprise-ai-coding-engineering/docs/metadata-standard
title: 文档与资产元数据规范
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: governance-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Spec", "Implementation", "Verification", "Review", "Learning"]
applicable_tools: ["Python"]
source_type: DECISION
evidence_level: DECISION
risk_level: LOW
supersedes: null
---

# 文档与资产元数据规范

## 目的

元数据让文档可发现、可校验、可审计，也避免把内容成熟度与采用建议混为一谈。Schema 位于 [`catalog/schemas`](../../catalog/schemas/)。

## 必填字段

```yaml
---
id: 组织内唯一、稳定的路径式 ID
title: 人类可读标题
version: 语义化版本
status: DRAFT | REVIEWED | VERIFIED | DEPRECATED | ARCHIVED
recommendation: RECOMMENDED | CONDITIONAL | NOT_RECOMMENDED | NOT_APPLICABLE | PENDING
owner: 负责维护的角色或团队
reviewers: []
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
applicable_stages: []
applicable_tools: []
source_type: OFFICIAL | EMPIRICAL | INDUSTRY | COMMUNITY | INFERENCE | DECISION
evidence_level: OFFICIAL | EMPIRICAL | INDUSTRY | COMMUNITY | INFERENCE | DECISION
risk_level: LOW | MEDIUM | HIGH | CRITICAL
supersedes: null
---
```

`status` 描述成熟度，`recommendation` 描述采用结论。例如某资产可以是 `VERIFIED`，但因成本或场景限制而是 `CONDITIONAL`。`source_type` 表示内容主要性质，`evidence_level` 表示支撑结论的最高证据级别。

## ID 与版本

- ID 使用小写路径式命名，发布后不因文件移动随意改变。
- ID 在所有受治理 Markdown 中唯一。
- 语义变化提升版本；仅排版修正可保留版本。
- 被替代内容保留历史，将状态改为 `DEPRECATED` 并填写 `supersedes` 或在正文链接后继文档。

## 时间、Owner 与审查

日期使用 ISO `YYYY-MM-DD`。Owner 是可承担维护职责的角色或团队，不使用模型名称。`reviewers` 记录实际完成审查者；未审查保持空数组，不虚构。

## 适用范围与例外

仓库自身的规范、报告、ADR 和目录说明均受治理。下列文件因用途特殊可由校验器排除完整元数据检查：

- 外部总控指令；
- `assets/templates/`、`research/templates/` 和 `reports/templates/` 中含占位变量的模板；
- 许可证正文。

例外不意味着内容可以绕过本地链接或敏感信息审查。
