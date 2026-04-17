# -*- coding: utf-8 -*-
from tarot_db import TAROT_DB

def generate_three_card_comprehensive(cards):
    """
    生成三牌阵的深度综合解读（神秘风格·层次分明版）
    """
    if len(cards) < 3:
        return "<p>错误：需要三张牌。</p>"

    # ========== 配色方案 ==========
    purple = '#9d4edd'
    red = '#ff6b6b'
    cyan = '#4ecdc4'
    gold = '#ffd700'
    text = '#e8e8e8'
    text_dim = '#a0a0a0'
    card_bg = 'rgba(26, 26, 46, 0.95)'
    border = 'rgba(157, 78, 221, 0.3)'

    # ========== 内容生成 ==========
    # 1. 核心主题
    theme = cards[0]['name'] + ' → ' + cards[1]['name'] + ' → ' + cards[2]['name']
    theme_desc = '从「' + cards[0]['coreEnergy'] + '」经「' + cards[1]['coreEnergy'] + '」到「' + cards[2]['coreEnergy'] + '」'

    # 2. 三牌展示
    def card_html(card, label, color):
        return '''
        <div style="flex: 1; text-align: center; padding: 20px 10px; background: ''' + card_bg + '''; border-radius: 12px; border: 1px solid ''' + color + '''33;">
            <div style="font-size: 42px; margin-bottom: 10px; filter: drop-shadow(0 0 8px ''' + color + '''44);">''' + card['emoji'] + '''</div>
            <div style="font-size: 14px; color: ''' + color + '''; margin-bottom: 4px; font-weight: bold;">''' + card['name'] + '''</div>
            <div style="font-size: 10px; color: ''' + text_dim + '''; letter-spacing: 2px;">''' + label + '''</div>
        </div>'''

    cards_html = card_html(cards[0], 'THE PAST', purple)
    cards_html += '<div style="display: flex; align-items: center; font-size: 20px; color: ' + gold + '''; padding: 0 8px;">⟡</div>'''
    cards_html += card_html(cards[1], 'THE PRESENT', red)
    cards_html += '<div style="display: flex; align-items: center; font-size: 20px; color: ' + gold + '''; padding: 0 8px;">⟡</div>'''
    cards_html += card_html(cards[2], 'THE FUTURE', cyan)

    # 3. 各板块内容
    sections = [
        {
            'title': '✧ Relationship Analysis',
            'subtitle': '关系分析',
            'color': purple,
            'content': '<span style="color: ' + purple + ''';">从''' + cards[0]['name'] + '''到''' + cards[2]['name'] + '''，</span>这是一个从「<span style="color: ''' + gold + ''';">''' + cards[0]['coreEnergy'] + '''</span>」到「<span style="color: ''' + gold + ''';">''' + cards[2]['coreEnergy'] + '''</span>」的完整旅程。<span style="color: ''' + red + ''';">''' + cards[1]['name'] + '''</span>正处于关键的转折点，它既是挑战，也是成长的契机。'''
        },
        {
            'title': '⚡ Energy Flow',
            'subtitle': '能量流向',
            'color': red,
            'content': '<span style="color: ' + purple + ''';">''' + cards[0]['emoji'] + ' ' + cards[0]['name'] + '''</span>：''' + cards[0]['coreEnergy'] + '''。<span style="color: ''' + text_dim + ''';">——你的能量根基</span><br><br>
                       <span style="color: ''' + red + ''';">''' + cards[1]['emoji'] + ' ' + cards[1]['name'] + '''</span>：''' + cards[1]['coreEnergy'] + '''。<span style="color: ''' + text_dim + ''';">——你正在经历的转化</span><br><br>
                       <span style="color: ''' + cyan + ''';">''' + cards[2]['emoji'] + ' ' + cards[2]['name'] + '''</span>：''' + cards[2]['coreEnergy'] + '''。<span style="color: ''' + text_dim + ''';">——能量的最终指向</span>'''
        },
        {
            'title': '✧ The Comprehensive Reading',
            'subtitle': '综合解读',
            'color': gold,
            'content': '<span style="color: ''' + text + ''';">这组牌揭示了一个深刻的能量演化过程。</span><br><br>
                       <span style="color: ''' + purple + ''';">起始于''' + cards[0]['name'] + '''</span>——''' + cards[0]['summary'] + '''。这代表了您过去所拥有的基础或初衷，是支撑您走到今天的能量根源。<br><br>
                       <span style="color: ''' + red + ''';">目前您正经历着''' + cards[1]['name'] + '''</span>——''' + cards[1]['summary'] + '''。这不仅仅是一个障碍，更是灵魂在向更高层次跨越前的必要考验。<br><br>
                       <span style="color: ''' + cyan + ''';">未来的''' + cards[2]['name'] + '''</span>正带着「''' + cards[2]['summary'] + '''」的能量向您走来，预示着一切努力终将获得圆满。'''
        },
        {
            'title': '🎯 Life Dimensions',
            'subtitle': '生活维度',
            'color': cyan,
            'content': '<span style="color: ' + purple + ''';">❤️ 爱情</span><br>''' + cards[0]['name'] + '''带来的纯真回忆正在滋养您，当前''' + cards[1]['name'] + '''的考验会让感情更加成熟，最终走向''' + cards[2]['name'] + '''的圆满。<br><br>
                       <span style="color: ''' + purple + ''';">💼 事业</span><br>过去的积累（''' + cards[0]['name'] + '''）正遭遇当前的挑战（''' + cards[1]['name'] + '''），但请坚持，''' + cards[2]['name'] + '''预示着突破性的成功。<br><br>
                       <span style="color: ''' + purple + ''';">🏥 健康</span><br>注意心理健康的调节，从''' + cards[1]['name'] + '''的焦虑中释放，找回生命的活力。<br><br>
                       <span style="color: ''' + purple + ''';">💰 财富</span><br>财务能量正在经历转化，从波动的阶段转向稳健丰盛的收获期。'''
        },
        {
            'title': '💡 Action Guide',
            'subtitle': '行动指南',
            'color': gold,
            'content': '<span style="color: ' + purple + ''';">1. 【接纳''' + cards[0]['name'] + '''】</span><br>''' + cards[0]['guidance'][:100] + '''...<br><span style="color: ''' + text_dim + ''';">思考：这份来自过去的能量如何支持你？</span><br><br>
                       <span style="color: ''' + red + ''';">2. 【拥抱''' + cards[1]['name'] + '''】</span><br>''' + cards[1]['guidance'][:100] + '''...<br><span style="color: ''' + text_dim + ''';">行动：今天如何主动参与这个转化过程？</span><br><br>
                       <span style="color: ''' + cyan + ''';">3. 【期待''' + cards[2]['name'] + '''】</span><br>''' + cards[2]['guidance'][:100] + '''...<br><span style="color: ''' + text_dim + ''';">态度：保持开放，相信最好的还在前方。</span>'''
        },
    ]

    sections_html = ''
    for s in sections:
        sections_html += '''
        <div style="margin-bottom: 16px; padding: 20px; background: ''' + card_bg + '''; border-radius: 12px; border-left: 3px solid ''' + s['color'] + '''; clear: both;">
            <div style="margin-bottom: 12px;">
                <span style="font-size: 12px; color: ''' + s['color'] + '''; letter-spacing: 2px; text-transform: uppercase;">''' + s['title'] + '''</span>
                <span style="font-size: 11px; color: ''' + text_dim + '''; margin-left: 8px;">''' + s['subtitle'] + '''</span>
            </div>
            <div style="font-size: 13px; color: ''' + text + '''; line-height: 1.9; font-family: Georgia, serif;">''' + s['content'] + '''</div>
        </div>'''

    # ========== 完整HTML ==========
    html = '''
<div style="display: block; width: 100%; max-width: 680px; margin: 0 auto; padding: 20px; font-family: Georgia, 'Times New Roman', serif; color: ''' + text + '''; line-height: 1.6;">

    <!-- 标题区 -->
    <div style="text-align: center; margin-bottom: 24px; padding: 24px; background: ''' + card_bg + '''; border-radius: 16px; border: 1px solid ''' + border + ''';">
        <div style="font-size: 14px; color: ''' + gold + '''; letter-spacing: 6px; margin-bottom: 12px;">✧ · ˚ ✦ · ˚ ✧</div>
        <div style="font-size: 11px; color: ''' + text_dim + '''; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 16px;">The Tarot Reading</div>
        <div style="font-size: 18px; color: ''' + text + '''; font-weight: normal; margin-bottom: 8px;">''' + theme + '''</div>
        <div style="font-size: 12px; color: ''' + text_dim + '''; font-style: italic;">''' + theme_desc + '''</div>
    </div>

    <!-- 三牌展示 -->
    <div style="display: flex; justify-content: center; align-items: stretch; gap: 8px; margin-bottom: 20px; padding: 16px; background: ''' + card_bg + '''; border-radius: 16px; border: 1px solid ''' + border + ''';">
        ''' + cards_html + '''
    </div>

    <!-- 分隔装饰 -->
    <div style="text-align: center; margin-bottom: 20px; color: ''' + gold + '''; letter-spacing: 8px; font-size: 10px;">✧ · ˚ ✦ · ˚ ✧</div>

    <!-- 各分析板块 -->
    ''' + sections_html + '''

    <!-- 底部金句 -->
    <div style="text-align: center; margin-top: 24px; padding: 24px; background: linear-gradient(135deg, ''' + card_bg + ''', rgba(45, 45, 75, 0.95)); border-radius: 16px; border: 1px solid ''' + gold + '''33; clear: both;">
        <div style="font-size: 10px; color: ''' + text_dim + '''; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 16px;">✧ Today's Wisdom</div>
        <div style="font-size: 15px; color: ''' + gold + '''; font-style: italic; margin-bottom: 16px;">"''' + cards[2]['goldSentence'] + '''"</div>
        <div style="font-size: 14px; color: #c0c0c0;">🌙 ✦ ☀️ ✦ 🌙</div>
    </div>

</div>'''
    return html