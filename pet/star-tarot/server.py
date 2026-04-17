#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 星契塔罗服务器 v2
# 使用 tarot_db.py 中的真实塔罗数据，生成深度解读

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
    """根据牌名在数据库中查找塔罗牌（改进版）"""
    if not name:
        return None, None
    
    name_clean = name.strip()
    # 移除序号前缀
    name_clean = re.sub(r'^[第\d]+[张号个]?', '', name_clean).strip()
    # 移除emoji
    name_clean = re.sub(r'[\U0001F300-\U0001F9FF]', '', name_clean).strip()
    
    # 牌名简化映射（五芒星/星币 等统一）
    shorthand = {
        '愚人': '愚者', '魔术师': '魔术师', '女祭司': '女祭司',
        '权杖一': '权杖王牌', '圣杯一': '圣杯王牌', '宝剑一': '宝剑王牌', '星币一': '星币王牌',
        '权杖二': '权杖二', '圣杯二': '圣杯二', '宝剑二': '宝剑二', '星币二': '星币二',
        '五芒星': '星币', '五芒星七': '星币七',
        '五芒星一': '星币王牌', '权杖王牌': '权杖王牌', '圣杯王牌': '圣杯王牌', '宝剑王牌': '宝剑王牌', '星币王牌': '星币王牌',
    }
    for k, v in shorthand.items():
        if k in name_clean:
            name_clean = name_clean.replace(k, v)
    
    # 精确匹配中文名
    for card_id, card_data in TAROT_DB.items():
        card_name = card_data['name']
        chinese_name = re.sub(r'\s*\(.*\)', '', card_name)
        if chinese_name == name_clean:
            return card_id, card_data
    
    # 前缀匹配
    for card_id, card_data in TAROT_DB.items():
        card_name = card_data['name']
        chinese_name = re.sub(r'\s*\(.*\)', '', card_name)
        if chinese_name.startswith(name_clean) or name_clean in chinese_name:
            return card_id, card_data
    
    # 关键词匹配
    if len(name_clean) >= 2:
        for card_id, card_data in TAROT_DB.items():
            for kw in card_data.get('keywords', []):
                if kw in name_clean and len(kw) >= 2:
                    return card_id, card_data
    
    # 最后：取前2个字匹配
    if len(name_clean) >= 2:
        short = name_clean[:2]
        for card_id, card_data in TAROT_DB.items():
            card_name = card_data['name']
            chinese_name = re.sub(r'\s*\(.*\)', '', card_name)
            if short in chinese_name:
                return card_id, card_data
    
    return None, None

def get_all_card_names():
    """返回所有牌的中文名列表"""
    names = []
    for card_id, card_data in TAROT_DB.items():
        name = re.sub(r'\s*\(.*\)', '', card_data['name'])
        names.append(name)
    return names

def generate_three_card_reading_v2(message):
    """生成三牌阵的AI深度解读 v2（充分利用数据库）"""
    
    positions = ['过去', '现在', '未来']
    colors = ['#a78bfa', '#c678dd', '#43e97b']
    
    cards = []
    for i, pos in enumerate(positions):
        card_info = {'position': pos, 'color': colors[i]}
        
        # 提取牌名
        pos_pattern = f"{pos}：「(.+?)」"
        match = re.search(pos_pattern, message)
        if match:
            card_name = match.group(1)
            card_info['raw_name'] = card_name
            
            # 查找数据库
            card_id, db_card = find_card_by_name(card_name)
            if db_card:
                card_info['name'] = db_card['name']
                card_info['emoji'] = db_card['emoji']
                card_info['suit'] = db_card.get('suit', '未知')
                card_info['keywords'] = db_card.get('keywords', [])
                card_info['summary'] = db_card.get('summary', '')
                card_info['coreEnergy'] = db_card.get('coreEnergy', '')
                card_info['guidance'] = db_card.get('guidance', '')
                card_info['goldSentence'] = db_card.get('goldSentence', '')
                card_info['db_source'] = card_id
            else:
                card_info['name'] = card_name
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
    
    # 生成能量主题
    themes = [c['keywords'][0] if c['keywords'] else '未知' for c in cards]
    energy_theme = ' → '.join(themes)
    
    # 牌组分析
    suits = [c.get('suit', '未知') for c in cards]
    suit_analysis = ""
    if len(set(suits)) == 1:
        suit_analysis = f"三张牌都属于【{suits[0]}】牌组，能量纯粹而集中。"
    else:
        suit_analysis = f"三张牌来自不同牌组：{'、'.join(set(suits))}，能量多元交织。"
    
    # 核心能量分析
    core_energies = [c['coreEnergy'] if c['coreEnergy'] else '未知' for c in cards]
    energy_flow = f"""<span style="color:{cards[0]['color']};">◀ {cards[0]['name']}</span>
　　<span class="text-gray-500">能量根源</span>
　　{core_energies[0]}

<span style="color:{cards[1]['color']};">● {cards[1]['name']}</span>
　　<span class="text-gray-500">能量转化</span>
　　{core_energies[1]}

<span style="color:{cards[2]['color']};">▶ {cards[2]['name']}</span>
　　<span class="text-gray-500">能量指向</span>
　　{core_energies[2]}"""
    
    # 三牌核心洞察
    insights = []
    for c in cards:
        insight = f"""<div class="mb-4">
<span style="color:{c['color']};" class="font-bold">{c['name']} {c['emoji']}</span>
<div class="ml-4 mt-2">
<div class="text-xs text-gray-500 mb-1">核心能量：{c['coreEnergy']}</div>
<div class="text-xs text-gray-500 mb-1">关键词：{' · '.join(c['keywords'])}</div>
<div class="text-sm mt-2 leading-relaxed">{c['summary']}</div>
</div>
</div>"""
        insights.append(insight)
    
    # 深度解读（直接使用guidance）
    guidances = []
    for c in cards:
        g = c.get('guidance', '')
        if g:
            guidances.append(f"""<div class="mb-4 p-3 bg-gray-50 rounded-lg">
<span style="color:{c['color']};" class="font-bold">{c['name']}</span>
<div class="text-sm mt-2 leading-relaxed text-gray-700">{g}</div>
</div>""")
    
    # 金句
    gold_sentences = [c.get('goldSentence', '') for c in cards if c.get('goldSentence')]
    
    # 行动建议
    actions = f"""1. 【接纳{cards[0]['name']}】
　　{cards[0]['coreEnergy']}
　　思考：这份能量如何在背后支持你？

2. 【拥抱{cards[1]['name']}】
　　{cards[1]['coreEnergy']}
　　行动：今天如何更好地参与这个转化？

3. 【期待{cards[2]['name']}】
　　{cards[2]['coreEnergy']}
　　态度：保持开放，结果会以最合适的方式出现"""
    
    reading = f"""
✨ 【三牌阵深度解读】✨

━━━━━━━━━━━━━━━━━━━━
🔮 能量主题
━━━━━━━━━━━━━━━━━━━━
{energy_theme}
<span class="block mt-2 text-xs text-gray-500">{suit_analysis}</span>

━━━━━━━━━━━━━━━━━━━━
⚡ 核心能量分析
━━━━━━━━━━━━━━━━━━━━
{energy_flow}

━━━━━━━━━━━━━━━━━━━━
📖 三牌核心洞察
━━━━━━━━━━━━━━━━━━━━
{''.join(insights)}

━━━━━━━━━━━━━━━━━━━━
🔮 深度解读
━━━━━━━━━━━━━━━━━━━━
{''.join(guidances)}

━━━━━━━━━━━━━━━━━━━━
💫 今日金句
━━━━━━━━━━━━━━━━━━━━
{' | '.join([f'<span class="text-ai">{g}</span>' for g in gold_sentences])}

━━━━━━━━━━━━━━━━━━━━
💡 整合行动指南
━━━━━━━━━━━━━━━━━━━━
{actions}

━━━━━━━━━━━━━━━━━━━━

🌟 记住：塔罗不是预言，而是镜像。
它照见的是你内在已经存在的答案。

有问题随时召唤小七！🐼
"""
    return reading.strip()

def generate_single_reading_v2(card_name):
    """生成单张牌的深度解读 v2"""
    
    card_id, db_card = find_card_by_name(card_name)
    
    if not db_card:
        return f"""✨ 【{card_name}】🃏

━━━━━━━━━━━━━━━━━━━━
📖 牌面解读
━━━━━━━━━━━━━━━━━━━━
这张牌的能量还未被记录...

━━━━━━━━━━━━━━━━━━━━
💫 今日提示
━━━━━━━━━━━━━━━━━━━━
有时候，未知也是一种可能性。
今天试着以开放的心态面对一切。
"""

    emoji = db_card.get('emoji', '🃏')
    name = db_card.get('name', card_name)
    suit = db_card.get('suit', '')
    keywords = db_card.get('keywords', [])
    summary = db_card.get('summary', '')
    core_energy = db_card.get('coreEnergy', '')
    guidance = db_card.get('guidance', '')
    gold_sentence = db_card.get('goldSentence', '')
    
    reading = f"""
✨ 【{name}】{emoji}

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
                reading = generate_three_card_reading_v2(message)
            else:
                # 单张牌解读
                card_name = "塔罗牌"
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
                
                reading = generate_single_reading_v2(card_name)
            
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
    print(f"星契塔罗服务器 v2 启动成功！")
    print(f"塔罗数据库已加载：{len(TAROT_DB)} 张牌")
    print(f"访问: http://localhost:{PORT}")
    server = HTTPServer(('0.0.0.0', PORT), TarotsHandler)
    server.serve_forever()