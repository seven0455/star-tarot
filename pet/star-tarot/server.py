#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 星契塔罗服务器 v3
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
    """根据牌名在数据库中查找塔罗牌（严格匹配版）"""
    if not name:
        return None, None
    
    # 清理输入
    name_clean = name.strip()
    name_clean = re.sub(r'^[第\d]+[张号个]?', '', name_clean).strip()
    name_clean = re.sub(r'[\U0001F300-\U0001F9FF]', '', name_clean).strip()
    
    # 标准化牌名
    replacements = {
        '愚人': '愚者',
        '权杖一': '权杖王牌', '圣杯一': '圣杯王牌', '宝剑一': '宝剑王牌', '星币一': '星币王牌',
        '权杖二': '权杖二', '圣杯二': '圣杯二', '宝剑二': '宝剑二', '星币二': '星币二',
        '权杖三': '权杖三', '圣杯三': '圣杯三', '宝剑三': '宝剑三', '星币三': '星币三',
        '权杖四': '权杖四', '圣杯四': '圣杯四', '宝剑四': '宝剑四', '星币四': '星币四',
        '权杖五': '权杖五', '圣杯五': '圣杯五', '宝剑五': '宝剑五', '星币五': '星币五',
        '权杖六': '权杖六', '圣杯六': '圣杯六', '宝剑六': '宝剑六', '星币六': '星币六',
        '权杖七': '权杖七', '圣杯七': '圣杯七', '宝剑七': '宝剑七', '星币七': '星币七',
        '权杖八': '权杖八', '圣杯八': '圣杯八', '宝剑八': '宝剑八', '星币八': '星币八',
        '权杖九': '权杖九', '圣杯九': '圣杯九', '宝剑九': '宝剑九', '星币九': '星币九',
        '权杖十': '权杖十', '圣杯十': '圣杯十', '宝剑十': '宝剑十', '星币十': '星币十',
        '五芒星': '星币', '五芒星七': '星币七', '五芒星六': '星币六', '五芒星九': '星币九',
    }
    for old, new in replacements.items():
        if old in name_clean:
            name_clean = name_clean.replace(old, new)
    
    # 完全匹配（最严格）
    for card_id, card_data in TAROT_DB.items():
        card_name = card_data['name']
        chinese_name = re.sub(r'\s*\(.*\)', '', card_name).strip()
        if chinese_name == name_clean:
            return card_id, card_data
    
    # 包含匹配（次严格）
    for card_id, card_data in TAROT_DB.items():
        card_name = card_data['name']
        chinese_name = re.sub(r'\s*\(.*\)', '', card_name).strip()
        # 完全包含
        if name_clean in chinese_name or chinese_name in name_clean:
            return card_id, card_data
    
    # 关键词匹配（兜底）
    if len(name_clean) >= 3:  # 至少3个字才用关键词匹配
        for card_id, card_data in TAROT_DB.items():
            for kw in card_data.get('keywords', []):
                if len(kw) >= 2 and kw == name_clean:
                    return card_id, card_data
    
    return None, None

def generate_three_card_reading_v3(message):
    """生成三牌阵的AI深度解读 v3（严格匹配 + 完整guidance）"""
    
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
                card_info['emoji'] = db_card.get('emoji', '🃏')
                card_info['suit'] = db_card.get('suit', '未知')
                card_info['keywords'] = db_card.get('keywords', [])
                card_info['summary'] = db_card.get('summary', '')
                card_info['coreEnergy'] = db_card.get('coreEnergy', '')
                card_info['guidance'] = db_card.get('guidance', '')
                card_info['goldSentence'] = db_card.get('goldSentence', '')
                card_info['matched'] = card_id
            else:
                card_info['name'] = card_name
                card_info['emoji'] = '🃏'
                card_info['keywords'] = ['未知']
                card_info['summary'] = '待发现的牌面'
                card_info['coreEnergy'] = '未知'
                card_info['guidance'] = '这张牌的能量还未被解读...'
                card_info['goldSentence'] = '静待揭示...'
                card_info['matched'] = None
        else:
            card_info['name'] = '未知牌'
            card_info['emoji'] = '🃏'
            card_info['keywords'] = ['未知']
            card_info['summary'] = '未能获取牌面信息'
            card_info['coreEnergy'] = '未知'
            card_info['guidance'] = '请重新抽取塔罗牌...'
            card_info['goldSentence'] = '未知'
            card_info['matched'] = None
        
        cards.append(card_info)
    
    # 能量主题
    themes = [c['keywords'][0] if c['keywords'] else '未知' for c in cards]
    energy_theme = ' → '.join(themes)
    
    # 牌组分析
    suits = [c.get('suit', '未知') for c in cards]
    suit_analysis = ""
    if len(set(suits)) == 1:
        suit_analysis = f"三张牌都属于【{suits[0]}】牌组，能量纯粹而集中。"
    else:
        suit_analysis = f"三张牌来自不同牌组：{'、'.join(set(suits))}，能量多元交织。"
    
    # 核心能量流向
    energy_flow = ""
    for c in cards:
        energy_flow += f"""<span style="color:{c['color']};">◀ {c['name']}</span>
　　{c['coreEnergy']}
"""
    
    # 三牌独立解读（完整guidance）
    card_readings = ""
    for c in cards:
        g = c.get('guidance', '')
        if not g:
            g = '这张牌的能量还未被完全解读...'
        
        card_readings += f"""
<div class="mb-6 p-4 bg-gradient-to-r from-gray-50 to-white rounded-xl border-l-4" style="border-color: {c['color']};">
<div class="flex items-center gap-2 mb-3">
<span class="text-2xl">{c['emoji']}</span>
<span class="font-bold text-lg" style="color: {c['color']};">{c['name']}</span>
</div>
<div class="text-xs text-gray-500 mb-2">⚡ {c['coreEnergy']}</div>
<div class="text-xs text-gray-400 mb-3">🔮 {' · '.join(c['keywords'])}</div>
<div class="text-sm leading-relaxed text-gray-700">{g}</div>
<div class="mt-3 pt-3 border-t border-gray-100 text-sm text-ai">✨ {c.get('goldSentence', '')}</div>
</div>"""
    
    # 整合解读
    readings_html = ""
    for i, c in enumerate(cards):
        position_text = ['过去', '现在', '未来'][i]
        readings_html += f"""
<div class="mb-4">
<div class="flex items-center gap-2 mb-2">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-white text-sm" style="background-color: {c['color']};">{i+1}</span>
<span class="font-bold" style="color: {c['color']};">{position_text}：{c['name']}</span>
</div>
<div class="ml-10 text-sm text-gray-600">
<div class="mb-1">⚡ {c['coreEnergy']}</div>
<div class="mb-1">🔮 {' · '.join(c['keywords'])}</div>
<div class="text-xs text-gray-500">匹配ID: {c.get('matched', 'None')}</div>
</div>
</div>"""
    
    reading = f"""
✨ 【三牌阵深度解读】✨

━━━━━━━━━━━━━━━━━━━━
📍 三牌位置确认
━━━━━━━━━━━━━━━━━━━━
{readings_html}

━━━━━━━━━━━━━━━━━━━━
🔮 能量主题
━━━━━━━━━━━━━━━━━━━━
{energy_theme}
{suit_analysis}

━━━━━━━━━━━━━━━━━━━━
⚡ 核心能量流向
━━━━━━━━━━━━━━━━━━━━
{energy_flow}

━━━━━━━━━━━━━━━━━━━━
📖 三牌完整解读
━━━━━━━━━━━━━━━━━━━━
{card_readings}

━━━━━━━━━━━━━━━━━━━━
💡 行动指引
━━━━━━━━━━━━━━━━━━━━
1. 【接纳{cards[0]['name']}】{cards[0]['coreEnergy']}
2. 【拥抱{cards[1]['name']}】{cards[1]['coreEnergy']}
3. 【期待{cards[2]['name']}】{cards[2]['coreEnergy']}

━━━━━━━━━━━━━━━━━━━━

🌟 记住：塔罗不是预言，而是镜像。
它照见的是你内在已经存在的答案。

有问题随时召唤小七！🐼
"""
    return reading.strip()

def generate_single_reading_v3(card_name):
    """生成单张牌的深度解读 v3"""
    
    card_id, db_card = find_card_by_name(card_name)
    
    if not db_card:
        return f"""✨ 【{card_name}】🃏

这张牌的能量还未被记录...
匹配失败，请检查牌名。"""

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
            
            if '过去：' in message and '现在：' in message and '未来：' in message:
                reading = generate_three_card_reading_v3(message)
            else:
                card_name = "塔罗牌"
                if '塔罗牌「' in message:
                    try:
                        start = message.find('塔罗牌「') + 4
                        end = message.find('」', start)
                        if end > start:
                            card_name = message[start:end]
                    except:
                        pass
                reading = generate_single_reading_v3(card_name)
            
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
    print(f"星契塔罗服务器 v3 启动成功！")
    print(f"塔罗数据库已加载：{len(TAROT_DB)} 张牌")
    print(f"访问: http://localhost:{PORT}")
    server = HTTPServer(('0.0.0.0', PORT), TarotsHandler)
    server.serve_forever()