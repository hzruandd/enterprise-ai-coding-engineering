---
id: enterprise-ai-coding-engineering/adr/0006
title: ADR-0006 暂不建设完整 Agent 平台
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: platform-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Architecture", "Plan", "Operation"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: HIGH
supersedes: null
---

# ADR-0006：当前阶段暂不建设完整 Agent 平台

- 决策状态：ACCEPTED
- 决策者：项目技术负责人（由总控指令授权）

## 背景

Orchestrator、Worker、Sandbox 和 Dashboard 的需求取决于真实任务、风险和集成环境。Phase 0–1 尚无试点证据，直接实现会形成高维护成本并模糊参考体系定位。

## 备选方案

1. 立即自研完整平台：展示快，但需求和边界未经验证。
2. 永不实现平台：避免成本，但无法给出后期参考实现。
3. 先定义治理和契约，经研究、Eval 与试点后在 Phase 6 决策实现范围。

## 决策

Phase 0–1 的 `platform/` 只记录职责和准入条件。完成 Phase 2–5 的研究、资产验证与非生产试点，并形成人类批准的 build-vs-buy 决策后，最早在 Phase 6 开发参考实现。

## 后果

- 当前不会有平台代码或伪造 Demo。
- 前期聚焦可移植的契约、Gate、Trace 和治理。
- 未来实现启动较晚，但能减少错误架构和供应商锁定。

## 验证与复审

Phase 5 退出时检查是否存在稳定需求、威胁模型、运维 Owner、预算与替代方案；不满足则继续延期。
