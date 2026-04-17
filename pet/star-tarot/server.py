#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 星契塔罗服务器
# 使用 tarot_db.py 中的真实塔罗数据

import urllib.parse
import json
import re
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8086
DIR = os.path.dirname(os.path.abspath(__file__))

# 导入塔罗数据库
from tarot_db import TAROT_DB

def find_card_by_name(name):
    """"根据牌名在数据库中查找塔罗牌"""
    # 清理牌名（去除emoji等）
    name_clean = name.strip()
    
    # 移除可能的序号前缀（如"1." 或 "第1张"）
    name_clean = re.sub(r'^[第\d]+[张号个]?', '', name_clean).strip()
    
    # 尝试直接匹配（去掉英文部分后匹配中文名）
    for card_id, card_data in TAROT_DB.items():
        card_name = card_data['name']
        # 提取中文名（去掉英文括号部分）
        chinese_name = re.sub(r'\s*\(.*\)', '', card_name)
        
        if chinese_name in name_clean or name_clean in chinese_name:
            return card_id, card_data
        
        # 也尝试关键词匹配
        for keyword in card_data['keywords']:
            if keyword in name_clean and len(keyword) >= 2:
                return card_id, card_data
    
    # 最后尝试部分匹配（只取前2个字）
    if len(name_clean) >= 2:
        short_name = name_clean[:2]
        for card_id, card_data in TAROT_DB.items():
            card_name = card_data['name']
            chinese_name = re.sub(r'\s*\(.*\)', '', card_name)
            if short_name in chinese_name:
                return card_id, card_data
    
    return None, None

def generate_three_card_reading(message):
    """生成三牌阵的AI深度解读（使用真实数据库）"""
    
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
            card_name = match.group(1)
            card_info['name'] = card_name
            
            # 尝试从数据库查找
            card_id, db_card = find_card_by_name(card_name)
            if db_card:
                card_info['emoji'] = db_card['emoji']
                card_info['keywords'] = db_card['keywords']
                card_info['summary'] = db_card['summary']
                card_info['coreEnergy'] = db_card['coreEnergy']
                card_info['guidance'] = db_card['guidance']
                card_info['goldSentence'] = db_card['goldSentence']
                card_info['db_source'] = card_id
            else:
                # 没找到，使用默认值
                card_info['emoji'] = '🃏'
                card_info['keywords'] = ['未知']
                card_info['summary'] = '待发现的牌面'
                card_info['coreEnergy'] = '未知'
                card_info['guidance'] = '这张牌的能量还未被解读...'
                card_info['goldSentence'] = '静待揭示...'
        else:
            card_info['name'] = '未知牌'
            card_info['emoji'] = '🃏'
            card_info['keywords'] = ['未知']
            card_info['summary'] = '未能获取牌面信息'
            card_info['coreEnergy'] = '未知'
            card_info['guidance'] = '请重新抽取塔罗牌...'
            card_info['goldSentence'] = '未知'
        
        cards.append(card_info)
    
    # 计算能量主题
    energy_themes = [c['keywords'][0] if c['keywords'] else '未知' for c in cards]
    energy_theme = ' → '.join(energy_themes)
    
    # 生成能量流向
    energy_flow = f"""
<span style="color:{cards[0]['color']};">◀ {cards[0]['name']}</span> 
　　能量根源：你携带的内在资源

<span style="color:{cards[1]['color']};">● {cards[1]['name']}</span>
　　能量转化：正在发生的转变

<span style="color:{cards[2]['color']};">▶ {cards[2]['name']}</span>
　　能量指向：即将显现的结果
"""
    
    # 整合三张牌的解读
    readings = []
    for c in cards:
        readings.append(f"""<span style="color:{c['color']};">【{c['name']}】</span>

核心能量：{c['coreEnergy']}
关键词：{' · '.join(c['keywords'])}

{c['guidance']}

✨ {c['goldSentence']}
""")
    
    # 整合解读
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
📖 三牌详细解读
━━━━━━━━━━━━━━━━━━━━

{readings[0]}

━━━━━━━━━━━━━━━━━━━━

{readings[1]}

━━━━━━━━━━━━━━━━━━━━

{readings[2]}

━━━━━━━━━━━━━━━━━━━━
💡 整合行动指南
━━━━━━━━━━━━━━━━━━━━

1. 【接纳过去】{cards[0]['name']}的能量不是负担，而是根基。
   思考：这个能量如何在你生命中支持你？

2. 【专注当下】{cards[1]['name']}正在你生命中展开。
   行动：今天如何更好地参与这个转化过程？

3. 【开放结果】{cards[2]['name']}是可能的未来。
   态度：保持开放，但不为结果而焦虑。

━━━━━━━━━━━━━━━━━━━━

🌟 记住：塔罗不是预言，而是镜像。
它照见的是你内在已经存在的答案。

有问题随时召唤小七！🐼
"""
    return reading.strip()

def generate_ai_reading(card_name, guidance, summary, core_energy, keywords):
    """生成单张牌的AI解读（使用真实数据库）"""
    
    # 尝试从数据库查找
    card_id, db_card = find_card_by_name(card_name)
    
    if db_card:
        card_name = db_card['name']
        guidance = db_card['guidance']
        summary = db_card['summary']
        core_energy = db_card['coreEnergy']
        keywords = db_card['keywords']
        gold_sentence = db_card['goldSentence']
        emoji = db_card['emoji']
    else:
        gold_sentence = '等待揭示...'
        emoji = '🃏'
    
    reading = f"""
✨ 【{card_name}】{emoji}

━━━━━━━━━━━━━━━━━━━━
📖 牌面解读
━━━━━━━━━━━━━━━━━━━━

{summary}

⚡ 核心能量：{core_energy}

🔮 关键词：{' · '.join(keywords)}

━━━━━━━━━━━━━━━━━━━━
🔮 小七深度解读
━━━━━━━━━━━━━━━━━━━━

{guidance}

━━━━━━━━━━━━━━━━━━━━
💫 今日金句
━━━━━━━━━━━━━━━━━━━━

「{gold_sentence}」

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
            
            # 检测是否是三牌阵请求
            if '过去：' in message and '现在：' in message and '未来：' in message:
                reading = generate_three_card_reading(message)
            else:
                # 单张牌解读
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
    print(f"塔罗数据库已加载：{len(TAROT_DB)} 张牌")
    print(f"访问: http://localhost:{PORT}")
    server = HTTPServer(('0.0.0.0', PORT), TarotsHandler)
    server.serve_forever()