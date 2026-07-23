---
id: enterprise-ai-coding-engineering/adr/0005
title: ADR-0005 元数据与 Schema 驱动
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: governance-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Spec", "Implementation", "Verification", "Learning"]
applicable_tools: ["Python", "JSON Schema"]
source_type: DECISION
evidence_level: DECISION
risk_level: MEDIUM
supersedes: null
---

# ADR-0005：元数据与 Schema 驱动

- 决策状态：ACCEPTED
- 决策者：项目技术负责人（由总控指令授权）

## 背景

仅靠文档约定容易产生 ID 冲突、状态漂移和字段缺失。引入数据库或重型框架对初始阶段又过度复杂。

## 备选方案

1. 自由 Markdown：易写但难以治理。
2. 数据库为主：查询强但提高部署和迁移成本。
3. Markdown + JSON Schema + 轻量 Catalog：人机兼容且可在 CI 校验。

## 决策

受治理文档使用统一 front matter，结构化记录使用 JSON Schema。Catalog 文件扩展名为 `.yaml`，内容使用 JSON 语法兼容的 YAML 1.2，Phase 0–1 校验器只依赖 Python 标准库。

## 后果

- 状态、推荐、风险和证据字段可机器检查。
- JSON 兼容写法牺牲部分 YAML 可读性，换取确定性和零依赖。
- 若未来需要完整 YAML 语法，必须明确依赖、锁定版本并新增迁移 ADR。

## 验证与复审

所有 Schema 必须可解析，Catalog 条目必须通过对应 Schema，文档 ID 不得重复。规模或查询需求显著增长时复审存储方式。
