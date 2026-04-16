# ERRORS.md - 小七的错误记录

## 2026-04-16 错误记录

### 错误1: WSL安装超时
**时间:** 2026-04-16 10:31
**类型:** exec SIGKILL (command timeout)
**上下文:** 尝试安装 WSL2 `wsl --install -d Ubuntu --web-download`
**原因:** Windows 10 Home China 环境，WSL 安装需要下载且耗时较长
**恢复:** 手动安装方案，已告知 Seven
**状态:** 待 Seven 手动安装 WSL2

### 错误2: openclaw status/exec 超时
**时间:** 2026-04-16 上午
**类型:** exec timeout
**上下文:** 多次 exec 命令超时或被 SIGKILL
**原因:** 可能是系统资源问题或命令设计问题
**恢复:** 改用简单的 netstat 检测服务状态
**状态:** 已改善

---

## 预防措施

1. exec 命令设置合理的 timeout
2. 优先使用轻量级检测命令
3. 长时间命令要后台运行

## 待解决

- [ ] WSL2 安装（需要 Seven 手动执行）
- [ ] Hermes 集成
