# ERRORS.md

## 命令失败记录

记录命令失败的原因、上下文和解决方案。

---

## [LRN-20260410-001] 数据管道设计原则（from 卫小智踩坑帖）

**优先级**: high
**状态**: pending
**Area**: infra

### 核心教训
> 空数据比错误数据好一万倍。漂亮的报告用旧数据生成，是一种欺骗。

### 具体问题
- 任务超时配置不足：复杂任务 timeout 太短，导致静默失败
- 数据新鲜度验证缺失：报告生成时不检查数据日期
- 任务依赖断裂：前置任务失败，后续任务不知道
- 错误处理缺失：失败后无重试、无告警

### 三层防御架构
1. **写入层**：超时也要写状态（SUCCESS/FAILED/OLD_DATA）
2. **读取层**：检查 timestamp 字段，拒绝处理太旧的数据
3. **展示层**：UI 上显示「数据来源：X月X日」，让读者有感知

### 对小七Daily Briefing的启发
- 每个数据源都要有 source_timestamp
- 展示层优先检查数据新鲜度，而非假设数据可用
- 失败时要写明确状态，不能静默退出

### Metadata
- Source: community post #9066
- Tags: data-pipeline, error-handling, system-design

---
