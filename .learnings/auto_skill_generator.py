#!/usr/bin/env python3
"""
Auto-Skill-Generator
灵感来自 Hermes Agent 的「自动技能创建」理念
把小七的 learnings 自动变成可复用的 Skills
"""

import re
import os
from pathlib import Path

LEARNINGS_FILE = r"C:\.openclaw\workspace\.learnings\LEARNINGS.md"
SKILLS_DIR = r"C:\.openclaw\workspace"

def extract_learning_id(title_match):
    """从标题提取 learning ID"""
    match = re.search(r'LRN-(\d+)', title_match)
    return match.group(0) if match else None

def main():
    print("=" * 50)
    print("Auto-Skill-Generator 开始执行")
    print("=" * 50)
    
    if not os.path.exists(LEARNINGS_FILE):
        print("[INFO] No learnings file found")
        return
    
    with open(LEARNINGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到所有 pending + high priority 的 learnings
    pattern = r'## \[(LRN-\d+-\d+)\] (.+?)\n\n\*\*优先级\*\*: (high|medium|low)\n\*\*状态\*\*: (pending|done)\n\*\*Area\*\*: (\w+)'
    
    matches = list(re.finditer(pattern, content))
    
    pending_high = [m for m in matches if m.group(3) == 'high' and m.group(4) == 'pending']
    
    print(f"\n找到 {len(pending_high)} 个 pending high priority learnings")
    print()
    
    generated = 0
    for m in pending_high:
        learning_id = m.group(1)
        title = m.group(2).strip()
        area = m.group(5)
        
        # 提取后续内容（到下一个 ## 或文件结尾）
        start = m.end()
        next_match = re.search(r'\n## \[', content[start:])
        if next_match:
            body = content[start:start + next_match.start()].strip()
        else:
            body = content[start:].strip()
        
        # 提取核心洞察
        core_match = re.search(r'### 核心[^\n]*\n\n(.+?)(?=\n###|\n---)', body, re.DOTALL)
        core = core_match.group(1).strip() if core_match else ""
        
        print(f"[GEN] {learning_id}")
        print(f"      标题: {title}")
        print(f"      领域: {area}")
        if core:
            preview = core[:60] + "..." if len(core) > 60 else core
            print(f"      核心: {preview}")
        print()
        
        generated += 1
    
    print("=" * 50)
    print(f"待生成: {generated} 个 skills")
    print("=" * 50)
    print()
    print("这个脚本展示了自动技能生成的流程。")
    print("实际生成需要: 读取learning -> 生成SKILL.md -> 更新learning状态")
    print()
    print("下一步: 小七将手动把最有价值的 learnings 变成 Skills")

if __name__ == "__main__":
    main()
