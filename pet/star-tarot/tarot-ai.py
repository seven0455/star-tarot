#!/usr/bin/env python3
"""
塔罗AI解读生成器
用Python内置urllib调用OpenClaw Gateway API
"""

import json
import urllib.request
import urllib.error

GATEWAY_URL = "http://127.0.0.1:18789"
TOKEN = "0e860ae09c3abf623bd3f49fbdae4d32213e1db3115fe0a7"

def call_llm(prompt):
    """调用llm-task"""
    data = json.dumps({
        "tool": "llm-task",
        "args": {
            "prompt": prompt,
            "temperature": 0.8,
            "maxTokens": 500
        }
    }).encode('utf-8')
    
    req = urllib.request.Request(
        f"{GATEWAY_URL}/tools/invoke",
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode('utf-8'))
        if result.get("ok"):
            return result["result"]["details"]["text"]
        else:
            return f"Error: {result.get('error', {}).get('message', 'Unknown')}"

def generate_interpretation(card_name, card_meaning, position="今日单张牌"):
    """生成塔罗牌解读"""
    
    prompt = f"""你是一个专业的塔罗解读师。用户抽到了 {card_name}。
    
牌面核心含义：{card_meaning}
抽牌位置：{position}

请生成一段150-200字的专业解读：
1. 结合牌义和位置的解读（30字左右）
2. 今日能量分析和建议（80字左右）
3. 一个积极的结束语（30字左右）

直接输出解读文字，简洁有温度。"""

    return call_llm(prompt)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("用法: python tarot-ai.py <牌名> <牌义> [位置]")
        sys.exit(1)
    
    card_name = sys.argv[1]
    card_meaning = sys.argv[2]
    position = sys.argv[3] if len(sys.argv) > 3 else "今日单张牌"
    
    result = generate_interpretation(card_name, card_meaning, position)
    print(result)
