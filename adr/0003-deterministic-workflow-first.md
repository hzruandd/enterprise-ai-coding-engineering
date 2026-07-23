---
id: enterprise-ai-coding-engineering/adr/0003
title: ADR-0003 确定性 Workflow 优先
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: architecture-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Plan", "Implementation", "Verification", "Release"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: HIGH
supersedes: null
---

# ADR-0003：确定性 Workflow 优先、Agentic 适量

- 决策状态：ACCEPTED
- 决策者：项目技术负责人（由总控指令授权）

## 背景

编译、测试、扫描和制品归档等步骤输入输出明确。让 Agent 动态决定这些步骤会增加不确定性、成本和审计难度；代码定位和根因分析则需要上下文判断。

## 备选方案

1. 全 Agentic：灵活，但结果和成本难预测。
2. 全固定脚本：可复现，但无法处理开放式问题。
3. 固定工作流骨架加受限 Agent 决策点：兼顾确定性和适应性。

## 决策

可预测环节使用确定性 Workflow；仅在步骤需要动态推理时授予 Agent 明确边界、预算和工具。发布、生产变更和权限提升保留人工审批。

## 后果

- 资产设计必须说明哪些步骤确定、哪些步骤允许 Agent 决策。
- 多 Agent 只在职责隔离、并行收益或独立验收明确时采用。
- 需要更多契约和状态管理，但可提高复现与审计能力。

## 验证与复审

Eval 比较任务成功率、人工接管率、时延和成本。若动态决策没有带来可测收益，应收敛为固定步骤。
