#!/usr/bin/env python3
# 星契塔罗服务器
import urllib.parse
import json
import re
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

import os
PORT = 8086
DIR = os.path.dirname(os.path.abspath(__file__))

def generate_three_card_reading(message):
    """生成三牌阵的AI深度解读"""
    # 解析三张牌的信息
    cards = []
    positions = ['过去', '现在', '未来']
    colors = ['#a78bfa', '#c678dd', '#43e97b']
    
    for i, pos in enumerate(positions):
        card_info = {'position': pos, 'color': colors[i]}
        
        # 提取牌名
        pos_pattern = f"{pos}：「(.+?)」"
        match = re.search(pos_pattern, message)
        if match:
            card_info['name'] = match.group(1)
        else:
            card_info['name'] = '未知牌'
        
        # 提取emoji
        emoji_match = re.search(f"{pos}：.+?([\U0001F300-\U0001F9FF])", message)
        if emoji_match:
            card_info['emoji'] = emoji_match.group(1)
        else:
            card_info['emoji'] = '🃏'
        
        # 提取关键词
        kw_match = re.search(f"{pos}.+?关键词: (.+?)\| ", message)
        if kw_match:
            card_info['keywords'] = kw_match.group(1).split(', ')
        else:
            card_info['keywords'] = []
        
        # 提取爱情、事业、健康、财运评分
        love_match = re.search(f"爱情:(\d)★", message)
        career_match = re.search(f"事业:(\d)★", message)
        health_match = re.search(f"健康:(\d)★", message)
        wealth_match = re.search(f"财运:(\d)★", message)
        
        card_info['love'] = int(love_match.group(1)) if love_match else 0
        card_info['career'] = int(career_match.group(1)) if career_match else 0
        card_info['health'] = int(health_match.group(1)) if health_match else 0
        card_info['wealth'] = int(wealth_match.group(1)) if wealth_match else 0
        
        # 提取解读
        meaning_match = re.search(f"解读: (.+?)(?:\n|$)", message)
        if meaning_match:
            card_info['meaning'] = meaning_match.group(1)
        else:
            card_info['meaning'] = ''
        
        cards.append(card_info)
    
    # 计算能量总分
    love_total = sum(c['love'] for c in cards)
    career_total = sum(c['career'] for c in cards)
    health_total = sum(c['health'] for c in cards)
    wealth_total = sum(c['wealth'] for c in cards)
    
    # 生成能量主题
    themes = []
    for c in cards:
        if c['keywords']:
            themes.append(c['keywords'][0])
    energy_theme = ' → '.join(themes) if themes else '待发现'
    
    # 分析能量流向
    energy_flow = f"""
<span style="color:{cards[0]['color']};">◀ {cards[0]['name']}</span> 
　　能量根源：你携带的内在资源

<span style="color:{cards[1]['color']};">● {cards[1]['name']}</span>
　　能量转化：正在发生的转变

<span style="color:{cards[2]['color']};">▶ {cards[2]['name']}</span>
　　能量指向：即将显现的结果
"""
    
    # 能量分析
    love_analysis = f"""你的爱情能量正经历「{'高' if love_total >= 10 else '中' if love_total >= 6 else '低'}强度」的流动。{'这张牌阵显示了感情发展的关键时刻，无论单身还是有伴，都能从中获得启示。' if love_total >= 8 else '感情方面需要更多耐心和理解，让自己和对方都有成长的空间。'}"""
    
    career_analysis = f"""事业能量显示为{'积极' if career_total >= 10 else '平稳' if career_total >= 6 else '需要调整'}状态。{'现在是你展现实力、迈向新阶段的良机。' if career_total >= 8 else '或许需要等待更好的时机，但持续的准备不会白费。'}"""
    
    # 行动建议
    actions = f"""1. 【接纳过去】{cards[0]['keywords'][0] if cards[0]['keywords'] else cards[0]['name']}的能量不是负担，而是根基。承认它，感谢它。

2. 【专注当下】{cards[1]['keywords'][0] if cards[1]['keywords'] else cards[1]['name']}正在你生命中展开。带着觉知参与其中，而非被动反应。

3. 【开放结果】{cards[2]['keywords'][0] if cards[2]['keywords'] else cards[2]['name']}是可能的未来，但不是唯一的结局。你的每一个选择都在塑造它。

4. 【整合能量】三张牌形成一个完整的转化圈——过去滋养现在，现在创造未来。"""
    
    reading = f"""
✨ 【三牌阵深度解读】✨

━━━━━━━━━━━━━━━━━━━━
🔮 能量主题
━━━━━━━━━━━━━━━━━━━━
{energy_theme}

━━━━━━━━━━━━━━━━━━━━
💫 能量流向分析
━━━━━━━━━━━━━━━━━━━━
{energy_flow}

━━━━━━━━━━━━━━━━━━━━
📊 维度能量解读
━━━━━━━━━━━━━━━━━━━━

💕 爱情：{'★' * round(love_total/3)}{'☆' * (5-round(love_total/3))} ({love_total}/15)
　　{love_analysis}

💼 事业：{'★' * round(career_total/3)}{'☆' * (5-round(career_total/3))} ({career_total}/15)
　　{career_analysis}

💪 健康：{'★' * round(health_total/3)}{'☆' * (5-round(health_total/3))} ({health_total}/15)
　　健康能量{'较强' if health_total >= 10 else '中等' if health_total >= 6 else '需要关注'}，记得给自己足够的休息和滋养。

💰 财运：{'★' * round(wealth_total/3)}{'☆' * (5-round(wealth_total/3))} ({wealth_total}/15)
　　财运能量{'显示机遇' if wealth_total >= 10 else '保持平稳' if wealth_total >= 6 else '暂时需要保守'}，但记住：真正的财富是创造价值的能力。

━━━━━━━━━━━━━━━━━━━━
🔮 三牌核心洞察
━━━━━━━━━━━━━━━━━━━━

<span style="color:{cards[0]['color']};">【{cards[0]['name']}】</span>揭示了你的内在资源——{cards[0]['meaning'] or '那些你已经拥有的力量'}

<span style="color:{cards[1]['color']};">【{cards[1]['name']}】</span>呈现当前的挑战——{cards[1]['meaning'] or '你正面临的生命课题'}

<span style="color:{cards[2]['color']};">【{cards[2]['name']}】</span>指向可能的结果——{cards[2]['meaning'] or '如果你选择正确道路的奖赏'}

这三张牌共同在说：你的过去不是限制，而是弹药；你的现在不是困境，而是舞台；你的未来不是命运，而是召唤。

━━━━━━━━━━━━━━━━━━━━
💡 整合行动指南
━━━━━━━━━━━━━━━━━━━━
{actions}
━━━━━━━━━━━━━━━━━━━━

🌟 记住：塔罗不是预言，而是镜像。
它照见的是你内在已经存在的答案。
愿这份解读成为你今天行动的燃料。

有问题随时召唤小七！🐼
"""
    return reading.strip()

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
            
            # 检测是否是三牌阵请求
            if '过去：' in message and '现在：' in message and '未来：' in message and '请从以下角度' in message:
                reading = generate_three_card_reading(message)
            else:
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
