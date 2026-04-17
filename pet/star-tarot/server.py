#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 星契塔罗服务器 v4
# 使用 tarot_db.py 中的真实塔罗数据
# 三牌综合解读使用 tarot_engine.py

import urllib.parse
import json
import re
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8086
DIR = os.path.dirname(os.path.abspath(__file__))

# 导入塔罗数据库
from tarot_db import TAROT_DB

# 导入三牌综合解读引擎
from tarot_engine import generate_three_card_comprehensive

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
        if name_clean in chinese_name or chinese_name in name_clean:
            return card_id, card_data
    
    # 模糊匹配 - 只输入单个词如"力量"时
    if len(name_clean) <= 4:
        for card_id, card_data in TAROT_DB.items():
            card_name = card_data['name']
            # 直接用牌名检查是否包含输入词
            if name_clean in card_name:
                return card_id, card_data
    
    return None, None

def extract_three_cards(message):
    """从消息中提取三张牌的信息"""
    positions = ['过去', '现在', '未来']
    cards = []
    
    for pos in positions:
        pos_pattern = f"{pos}：「(.+?)」"
        match = re.search(pos_pattern, message)
        if match:
            card_name = match.group(1)
            card_id, db_card = find_card_by_name(card_name)
            
            if db_card:
                card_info = {
                    'name': db_card['name'],
                    'emoji': db_card.get('emoji', '🃏'),
                    'suit': db_card.get('suit', '未知'),
                    'keywords': db_card.get('keywords', []),
                    'summary': db_card.get('summary', ''),
                    'coreEnergy': db_card.get('coreEnergy', ''),
                    'guidance': db_card.get('guidance', ''),
                    'goldSentence': db_card.get('goldSentence', '')
                }
            else:
                card_info = {
                    'name': card_name,
                    'emoji': '🃏',
                    'suit': '未知',
                    'keywords': ['未知'],
                    'summary': '待发现的牌面',
                    'coreEnergy': '未知',
                    'guidance': '这张牌的能量还未被解读...',
                    'goldSentence': '静待揭示...'
                }
            cards.append(card_info)
        else:
            cards.append({
                'name': '未知牌',
                'emoji': '🃏',
                'suit': '未知',
                'keywords': ['未知'],
                'summary': '未能获取牌面信息',
                'coreEnergy': '未知',
                'guidance': '请重新抽取塔罗牌...',
                'goldSentence': '未知'
            })
    
    return cards

def generate_three_card_reading_v4(message):
    """生成三牌阵的深度综合解读 v4（使用 tarot_engine）"""
    
    cards = extract_three_cards(message)
    
    if len(cards) != 3:
        return "❌ 未能正确提取三张牌，请重试。"
    
    # 使用 tarot_engine 生成综合解读
    html_content = generate_three_card_comprehensive(cards)
    
    return html_content

def generate_single_reading(card_name):
    """生成单张牌的深度解读"""
    
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
            
            # 检测是否是三牌阵请求
            if '过去：' in message and '现在：' in message and '未来：' in message:
                reading = generate_three_card_reading_v4(message)
            else:
                # 单张牌解读 - 多种格式兼容
                card_name = None
                
                # 格式1: 塔罗牌「xxx」
                if not card_name and '塔罗牌「' in message:
                    try:
                        start = message.find('塔罗牌「') + 4
                        end = message.find('」', start)
                        if end > start:
                            card_name = message[start:end].strip()
                    except:
                        pass
                
                # 格式2: 牌名：xxx
                if not card_name and '牌名：' in message:
                    try:
                        start = message.find('牌名：') + 3
                        end = message.find('\n', start)
                        if end > start:
                            card_name = message[start:end].strip()
                    except:
                        pass
                
                # 格式3: 用户抽到的牌是：「xxx」
                if not card_name and '用户抽到的牌是：' in message:
                    try:
                        start = message.find('用户抽到的牌是：') + 8
                        end = message.find('」', start)
                        marker = message.find('（', start)
                        if marker > start and marker < end:
                            end = marker
                        if end > start:
                            card_name = message[start:end].strip()
                    except:
                        pass
                
                # 格式4: 牌是：「xxx」（xxx）
                if not card_name and '牌是：' in message:
                    try:
                        start = message.find('牌是：') + 3
                        end = message.find('）', start)
                        marker = message.find('（', start)
                        if marker > start and marker < end:
                            end = marker
                        if end > start:
                            card_name = message[start:end].strip()
                    except:
                        pass
                
                # 格式5: 「xxx」直接提取（兜底）
                if not card_name:
                    match = re.search(r'「([^」]+)」', message)
                    if match:
                        potential = match.group(1).strip()
                        # 验证是否是塔罗牌关键词
                        keywords = ['力量', '愚者', '魔术师', '女祭司', '皇后', '皇帝', '教皇', '恋人', '战车', '命运', '正义', '吊人', '死神', '节制', '恶魔', '塔', '星星', '月亮', '太阳', '审判', '世界', '权杖', '圣杯', '宝剑', '星币', '金币']
                        if any(k in potential for k in keywords):
                            card_name = potential
                
                card_name = card_name or "塔罗牌"
                reading = generate_single_reading(card_name)
            
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
    print(f"星契塔罗服务器 v4 启动成功！")
    print(f"塔罗数据库已加载：{len(TAROT_DB)} 张牌")
    print(f"三牌综合解读引擎已加载")
    print(f"访问: http://localhost:{PORT}")
    server = HTTPServer(('0.0.0.0', PORT), TarotsHandler)
    server.serve_forever()