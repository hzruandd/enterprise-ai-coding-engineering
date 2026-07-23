---
id: enterprise-ai-coding-engineering/adr/0001
title: ADR-0001 仓库定位与六能力域
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: architecture-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Idea", "Requirement", "Architecture", "Learning"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: MEDIUM
supersedes: null
---

# ADR-0001：仓库定位与六能力域

- 决策状态：ACCEPTED
- 决策者：项目技术负责人（由总控指令授权）

## 背景

企业采用 AI Coding 同时涉及知识、研发方法、可复用资产、治理、效果评价和运行平台。若仓库只做链接或 Prompt 收集，无法形成执行闭环；若直接建设平台，又会在需求未经验证前固化错误假设。

## 备选方案

1. Awesome List：维护简单，但不能给出采用证据和门禁。
2. 单一 Agent 平台：可演示运行能力，但覆盖不了方法、治理和研究。
3. 六能力域参考体系：范围较广，需要阶段控制，但能建立端到端闭环。

## 决策

仓库唯一定位为企业软件研发全生命周期的 AI Coding 工程化参考体系。使用 Knowledge、Methodology、Assets、Governance、Evaluation、Platform 六个能力域组织长期建设，并统一映射到项目定义的软件交付生命周期。

## 后果

- 所有新增内容必须明确所属能力域和生命周期阶段。
- 仓库不能退化为资源堆积或演示项目。
- 六域是能力地图，不要求提前创建全部目录或平均投入。

## 验证与复审

每个 Phase 验收检查定位与非目标一致性。若试点证明能力域缺失或重叠严重，通过新 ADR 复审。
