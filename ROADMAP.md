---
id: enterprise-ai-coding-engineering/roadmap
title: 建设路线图
version: 0.2.0
status: REVIEWED
recommendation: RECOMMENDED
owner: technical-lead
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Idea", "Plan", "Acceptance", "Learning"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: MEDIUM
supersedes: null
---

# 建设路线图

路线图使用阶段 Gate 控制范围。后续阶段不能因目录已经存在而视为已启动。

| Phase | 目标 | 关键产物 | 退出条件 | 当前状态 |
|---|---|---|---|---|
| 0 立项与边界 | 明确定位、对象、范围和非目标 | 章程、成功标准、决策边界 | 定位一致且待决策项显式化 | 完成 |
| 1 顶层架构与骨架 | 建立治理、分层、Schema、模板和校验 | 顶层文档、ADR、Catalog、校验器 | 仓库校验通过并形成验收证据 | 完成 |
| 2 研究与 Triage | 对优先主题建立事实记录和候选池 | 来源登记、Triage、比较矩阵 | 入围理由、许可证和访问状态清晰 | 完成（首批 8 项） |
| 3 方法与资产设计 | 将入围实践转为可执行契约 | 方法文档、Candidate 资产、Eval 设计 | 输入输出、Gate、风险和测试完整 | 未启动 |
| 4 验证与基线 | 在隔离环境运行真实任务 | Dataset、Baseline、Trace、Full Review | 可复现结果与独立审查完成 | 未启动 |
| 5 企业试点 | 在非生产真实场景评估采用效果 | 案例、采用指南、度量与复盘 | 价值、风险、成本均有试点证据 | 未启动 |
| 6 平台参考实现 | 仅在需求被验证后实现 Harness 组件 | Orchestrator/Worker/Sandbox 等参考实现 | 契约、测试、安全与运维门禁通过 | 未启动 |

## Phase 2 建议进入条件

1. Phase 0–1 验收报告经人类确认。
2. 明确首批研究主题、时间预算和责任人。
3. 用户提供或批准首批来源；不得由热度替代选择依据。
4. Triage 只做必要事实核验，不对全部候选执行 Full Review。
5. 任何下载、登录、付费或许可证不明的内容单独审批。

## 持续度量

从 Phase 2 起跟踪：来源访问状态、Candidate 转化率与淘汰率、证据完整率、文档陈旧率、重复资产、Gate 失败分布；从试点起增加任务成功率、一次通过率、人工接管率、交付时长、Token 与单位成果成本。

## Phase 2 完成摘要

首批 20 个官方来源均完成访问状态、来源类型和核验日期登记；8 个项目完成定位、许可证/条款、维护状态、适用场景和初步行动 Triage。4 项进入 PoC 设计队列，4 项先进入 Full Review 队列；没有提前创建 Candidate 资产。

Phase 3 仍未启动。进入条件是人类接受 [Phase 2 验收报告](reports/phase-2-acceptance.md)，并确认 PoC 可用的非生产环境、模型/工具预算和 License/Security Reviewer。
