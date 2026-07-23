---
id: enterprise-ai-coding-engineering/contributing
title: 贡献指南
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: technical-lead
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Requirement", "Plan", "Implementation", "Verification", "Review", "Learning"]
applicable_tools: ["Git", "Python"]
source_type: DECISION
evidence_level: DECISION
risk_level: LOW
supersedes: null
---

# 贡献指南

## 开始前

1. 阅读 [项目章程](PROJECT_CHARTER.md)、[治理规则](GOVERNANCE.md) 和适用 ADR。
2. 检查工作区，在独立分支或 worktree 工作，不覆盖未知变更。
3. 写明目标、非目标、验收标准、权限和影响范围。
4. 选择正确区域：事实记录进入 `research/`，Candidate 进入 `staging/`，只有 Verified 进入 `assets/`。

## 文档与证据

受治理的 Markdown 文档使用 [元数据规范](docs/overview/metadata-standard.md)。重要事实给出来源与访问状态；推断标为 `INFERENCE`，工程取舍标为 `DECISION`。不得把用户说明、搜索摘要或项目热度写成已验证事实。

## 外部项目流程

1. 来源登记：保留原始 URL、类型、访问状态和用户原注。
2. Triage：只核验官方入口/README、定位、许可证、维护状态、场景和初步行动。
3. Candidate：通过 Triage 后进入 `staging/`，定义 PoC 与淘汰条件。
4. Full Review：仅对入围项检查架构、维护、测试、安装、安全、商业风险和替代方案。
5. Verified：真实任务可复现、独立审查、License 核验且 Gate 通过后，才能移入 `assets/`。

## 可执行资产

资产必须具备唯一 ID、目标/非目标、触发器、输入输出契约、权限、步骤、Gate、失败处理、工具版本、示例、测试/Eval、变更记录、Owner、证据、安全和成本说明。使用 [资产模板](assets/templates/asset.md) 并通过 `catalog/schemas/asset.schema.json`。

## ADR

影响定位、边界、跨目录契约、安全、依赖或长期维护成本的决策应提交 ADR。ADR 先为 `PROPOSED`，经授权 Reviewer 接受后为 `ACCEPTED`；被替代时保留历史并链接后继 ADR。

## 验证与提交

运行：

```bash
python scripts/validate/validate_repository.py
```

只有退出码为 0 且完成差异自审后才能提交。使用 Conventional Commits，一个逻辑变更一个提交；不要自动 push、merge 或 release。许可证、生产访问、真实密钥和破坏性操作必须先获人工批准。
