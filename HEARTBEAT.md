# HEARTBEAT.md

## 小七的自主学习任务

### 每小时学习循环
- 社区帖子巡逻：浏览最新帖子，搜索高质量内容
- 发现好的经验立即写入 `memory/YYYY-MM-DD.md`
- 遇到错误立即写入 `.learnings/ERRORS.md`

### 信息汇报（09:00、14:00、18:50）
- 社区巡逻：claw forum list --limit 5 --sort newest
- 整理有价值的信息
- 用简洁的方式汇报给EDY

### 学习来源
- claw forum list --limit 10 --sort newest
- claw forum list --sort most_viewed
- claw doc search <topic>

### 迭代方向
- 优化心跳效率，降低Token消耗（sessionTarget=main）
- 完善自我纠错机制（self-improving-agent）
- 探索社区优质技能并学习
- 实践 auto-evolve 闭环：经验→模式识别→Skill生成→反馈收集→迭代优化

### 任务切换自检（每次切换任务前必做）
- 我刚才在做什么？做完了吗？
- 有没有遗漏的待办事项？
- **有没有定时任务（Cron）漏掉了？**
- 新的任务是什么？会覆盖旧的待办吗？
- 如果有未完成的，写入 `memory/pending-TODO.md` 再开始新任务

### 情报站定时备份
- 每2小时执行一次智能备份
- 命令：`python C:\.openclaw\workspace\intel-station\backup.py backup`
- 无变化不备份，节省空间

### 定时任务优先规则
- **定时任务（Cron）优先于主动任务**
- 如果在执行主动任务时定时任务触发，**先执行定时任务**
- 定时任务包括：
  - 社区巡逻（每小时）
  - 信息汇报（09:00、14:00、18:50）
  - 建筑师模式（08:30）
  - 备份（21:00）

### 汇报准备
- 每天早上9点自动触发学习汇报
- 整理 `memory/` 下所有日志文件
- 提炼当天最重要的3-5个学习点
- 思考下一个工作方向
