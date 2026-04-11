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

## [LRN-20260411-002] 任务切换时丢失待办（from EDY反馈）

**优先级**: high
**状态**: closed
**Area**: self-management

### 核心教训
> 切换任务时容易忘记原来的待办事项。需要"出发前检查"和"待办清单"机制。

### 具体问题
- 回复帖子评论时太投入，忘记了"发帖求助图片问题"这个待办
- 没有"待办清单"记录当前会话中所有pending的事项
- 做完一件事后没有检查"还有什么没做完"

### 解决方案
1. **出发前检查**：每次切换任务前，回顾"还有什么没做完"
2. **待办清单**：把pending事项写入 `memory/pending-TODO.md`
3. **交接记录**：从A任务切换到B任务前，把A的未完成状态显式记录

### 具体行动
在 HEARTBEAT.md 中新增「任务切换自检」步骤：
- 切换任务前检查pending事项
- 未完成的写入 `memory/pending-TODO.md`

### Metadata
- Source: EDY feedback
- Tags: self-management, task-switching, discipline
