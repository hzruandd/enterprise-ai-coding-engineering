---
id: enterprise-ai-coding-engineering/project-charter
title: 项目章程
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: technical-lead
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Idea", "Requirement", "Architecture", "Acceptance", "Learning"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: LOW
supersedes: null
---

# 项目章程

## 使命

面向企业软件研发全生命周期，建设一套可执行、可验证、可审计、可治理、可持续演进的 AI Coding 工程化参考体系，并提供经过验证的规范、资产、评测方法与参考实现。

## 服务对象与价值

- 研发团队：获得可直接执行的工作流、模板、Gate 与失败处理规则。
- 技术管理者：获得权限、成本、质量、风险和采用效果的治理依据。
- 平台与效能团队：获得 Harness 能力契约、评测基线和集成边界。
- 安全与合规角色：获得审批点、证据链、许可证与暴露面检查机制。

## 范围

长期范围由 Knowledge、Methodology、Assets、Governance、Evaluation、Platform 六个能力域组成。所有交付物必须映射到唯一软件交付生命周期，并围绕模型外部的 Harness 建立输入输出契约、上下文、工具权限、状态机、验证、审查、Trace 和人工接管。

## 非目标

- 不训练或托管大模型。
- 不把仓库建设成链接集合、概念百科或大批量 Prompt/Skill 仓库。
- 不复制第三方项目形成资源堆积。
- 不以 Agent Demo 代替企业治理和可复现实证。
- Phase 0–1 不建设完整 Agent 平台、不连接生产环境、不批量抓取外部内容。

## 原则

1. 确定性 Workflow 处理可预测步骤，Agent 只承担需要动态判断的环节。
2. AI 不得自证完成；完成结论必须依赖独立、可复现的证据。
3. 默认最小权限，高风险写操作与生产相关动作必须人工审批。
4. 外部内容必须经历 `Research → Candidate → Verified`。
5. 成熟度 `status` 与采用建议 `recommendation` 分离。
6. 重要结论区分事实证据与项目决策，不伪造权威来源。

## Phase 0–1 成功标准

- 顶层定位、治理、路线图和贡献流程可指导后续贡献者。
- Research、Candidate、Verified 具备物理隔离和准入规则。
- 文档、来源、项目评估、资产、Task/Run 均有机器可校验契约。
- 关键架构决策有 ADR，且 Phase 边界明确。
- 统一校验入口可在无第三方依赖的环境中运行并通过。
- 验收报告只陈述有证据支持的完成情况。

## 决策与变更

定位、非目标、许可证、生产访问和高风险权限变更必须由人类负责人批准。其他变更遵循 [贡献指南](CONTRIBUTING.md) 和 [治理规则](GOVERNANCE.md)，重大技术取舍通过 ADR 记录。
