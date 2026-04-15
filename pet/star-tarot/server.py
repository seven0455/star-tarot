#!/usr/bin/env python3
# 星契塔罗服务器
import urllib.parse
import json
import re
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8086
DIR = r"C:\.openclaw\workspace\pet\star-tarot"

def generate_ai_reading(card_name, guidance, summary, core_energy, keywords):
    """基于深度guidance生成AI解读"""
    
    # 清理guidance中的特殊字符
    if guidance:
        guidance = guidance.strip()
        # 保持格式但确保可读性
        guidance = re.sub(r'\n{3,}', '\n\n', guidance)
    else:
        guidance = f"""
🌊 【关于今天，你要知道的事】

今天你抽到了 {card_name}。

这张牌在告诉你： Life is happening for you, not to you.
不管今天发生什么，都是你成长的一部分。

【小七的解读】

牌面虽然没有给出具体的指引，但记住：重要的不是你抽到什么牌，
而是你如何解读这张牌，以及如何把这份解读应用在你的生活中。

【今日课题】

找一个今天你遇到的挑战，换一个角度看待它。
不是"为什么发生在我身上"，而是"这件事想教我什么"。
"""
    
    reading = f"""
✨ 【{card_name}】✨

━━━━━━━━━━━━━━━━━━━━
📖 牌面解读
━━━━━━━━━━━━━━━━━━━━

{summary if summary else '今日的能量正在引导你...'}

⚡ 核心能量：{core_energy if core_energy else '等待被发现'}

🔮 关键词：{' · '.join(keywords) if keywords else '待发现'}

━━━━━━━━━━━━━━━━━━━━
🔮 小七深度解读
━━━━━━━━━━━━━━━━━━━━

{guidance}

━━━━━━━━━━━━━━━━━━━━
💫 今日金句
━━━━━━━━━━━━━━━━━━━━

「{summary if summary else '保持内心的光，黑暗终将消散。'}」

━━━━━━━━━━━━━━━━━━━━

🌟 牌面是你内在的镜子
愿这份解读给你带来启发
有问题随时召唤小七！🐼
"""
    return reading.strip()

class TarotsHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = urllib.parse.parse_qs(post_data)
            message = data.get('message', [''])[0]
            
            # 从消息中提取牌信息
            card_name = "塔罗牌"
            guidance = ""
            summary = ""
            core_energy = ""
            keywords = []
            
            # 提取牌名
            if '塔罗牌「' in message:
                try:
                    start = message.find('塔罗牌「') + 4
                    end = message.find('」', start)
                    if end > start:
                        card_name = message[start:end]
                except:
                    pass
            elif '牌名：' in message:
                try:
                    start = message.find('牌名：') + 3
                    end = message.find('\n', start)
                    if end > start:
                        card_name = message[start:end].strip()
                except:
                    pass
            
            # 提取关键词
            if '关键词：' in message:
                try:
                    start = message.find('关键词：') + 4
                    end = message.find('\n', start)
                    if end > start:
                        kw_text = message[start:end].strip()
                        if '、' in kw_text:
                            keywords = [k.strip() for k in kw_text.split('、') if k.strip()]
                except:
                    pass
            
            # 提取牌面含义
            if '牌面含义：' in message:
                try:
                    start = message.find('牌面含义：') + 5
                    # 找下一个\n之前的内容
                    remaining = message[start:]
                    end = remaining.find('\n')
                    if end > 0:
                        summary = remaining[:end].strip()
                    else:
                        summary = remaining.strip()
                except:
                    pass
            
            # 提取核心能量
            if '核心能量：' in message:
                try:
                    start = message.find('核心能量：') + 5
                    remaining = message[start:]
                    end = remaining.find('\n')
                    if end > 0:
                        core_energy = remaining[:end].strip()
                    else:
                        core_energy = remaining.strip()
                except:
                    pass
            
            # 提取今日指引 - 这是最重要的部分
            if '今日指引：' in message:
                try:
                    start = message.find('今日指引：') + 5
                    # 今日指引可能很长，找下一个"请给出"之前的内容
                    end = message.find('请给出', start)
                    if end > start:
                        guidance = message[start:end].strip()
                    else:
                        # 如果没找到，就取到消息结尾
                        guidance = message[start:].strip()
                    # 清理HTML标签
                    guidance = re.sub(r'<[^>]+>', '', guidance)
                except:
                    pass
            
            # 生成解读
            reading = generate_ai_reading(card_name, guidance, summary, core_energy, keywords)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'reply': reading}).encode('utf-8'))
        else:
            self.send_error(404)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    print(f"星契塔罗服务器启动成功！")
    print(f"访问: http://localhost:{PORT}")
    server = HTTPServer(('0.0.0.0', PORT), TarotsHandler)
    server.serve_forever()
