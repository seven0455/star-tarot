# -*- coding: utf-8 -*-
from tarot_db import TAROT_DB

def generate_three_card_comprehensive(cards):
    """
    生成三牌阵的深度综合解读（神秘风格，修复布局问题）
    """
    if len(cards) < 3:
        return "<p>错误：需要三张牌。</p>"

    # 神秘风格配色
    colors = {
        'bg': 'transparent',           # 透明背景，融入页面
        'card_bg': 'rgba(26, 26, 46, 0.95)',      # 卡片背景
        'accent1': '#9d4edd',      # 神秘紫
        'accent2': '#ff6b6b',      # 玫瑰红
        'accent3': '#4ecdc4',      # 星光青
        'gold': '#ffd700',         # 金色
        'silver': '#c0c0c0',       # 银色
        'text': '#e8e8e8',         # 主文字
        'text_dim': '#a0a0a0',     # 次文字
    }

    # 三牌总览
    overview = f"{cards[0]['name']} → {cards[1]['name']} → {cards[2]['name']}"

    # 关系分析
    rel_analysis = f"从「{cards[0]['coreEnergy']}」到「{cards[2]['coreEnergy']}」，{cards[1]['name']}处于转折点。"

    # 能量流向
    energy0 = f"{cards[0]['emoji']} {cards[0]['name']}：{cards[0]['coreEnergy']}。"
    energy1 = f"{cards[1]['emoji']} {cards[1]['name']}：{cards[1]['coreEnergy']}。"
    energy2 = f"{cards[2]['emoji']} {cards[2]['name']}：{cards[2]['coreEnergy']}。"

    # 综合解读
    text = f"""这组牌揭示了从{cards[0]['name']}到{cards[2]['name']}的演化过程。
起始于{cards[0]['summary']}，这是支撑你的能量根源。
目前经历{cards[1]['name']}——{cards[1]['summary']}，这是成长的考验。
未来指向{cards[2]['name']}——{cards[2]['summary']}，预示圆满。"""

    # 维度
    love = f"感情从{cards[0]['name']}的纯真出发，经{cards[1]['name']}的考验，走向{cards[2]['name']}的成熟。"
    work = f"事业：{cards[0]['name']}积累遭遇{cards[1]['name']}的挑战，{cards[2]['name']}预示突破。"
    health = f"健康：调节{cards[1]['name']}带来的压力，重拾{cards[2]['name']}的活力。"
    money = f"财富：从波动转向稳健，{cards[2]['name']}带来丰盛。"

    # 行动
    action0 = f"【接纳{cards[0]['name']}】{cards[0]['guidance'][:80]}..."
    action1 = f"【拥抱{cards[1]['name']}】{cards[1]['guidance'][:80]}..."
    action2 = f"【期待{cards[2]['name']}】{cards[2]['guidance'][:80]}..."

    # 修复：使用block显示，不覆盖其他内容
    html = f"""
<div style="display: block; width: 100%; max-width: 700px; margin: 20px auto; padding: 0; font-family: 'Georgia', 'Times New Roman', serif; color: {colors['text']}; line-height: 1.6;">
    
    <!-- 神秘标题 -->
    <div style="text-align: center; margin-bottom: 25px; padding: 20px; background: {colors['card_bg']}; border-radius: 16px; border: 1px solid {colors['accent1']}33;">
        <div style="font-size: 18px; color: {colors['gold']}; letter-spacing: 4px; margin-bottom: 8px;">✧ ✦ ✧</div>
        <div style="font-size: 12px; color: {colors['text_dim']}; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 12px;">Tarot Reading</div>
        <div style="font-size: 16px; color: {colors['accent1']}; font-weight: normal;">{overview}</div>
    </div>

    <!-- 三牌展示 -->
    <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 20px; padding: 20px; background: {colors['card_bg']}; border-radius: 16px; border: 1px solid {colors['accent1']}22;">
        <div style="flex: 1; text-align: center; padding: 15px 8px;">
            <div style="font-size: 36px; margin-bottom: 8px;">{cards[0]['emoji']}</div>
            <div style="font-size: 13px; color: {colors['accent1']}; margin-bottom: 4px;">{cards[0]['name']}</div>
            <div style="font-size: 10px; color: {colors['text_dim']}; letter-spacing: 1px;">PAST</div>
        </div>
        <div style="font-size: 18px; color: {colors['gold']}; padding: 0 5px;">⟡</div>
        <div style="flex: 1; text-align: center; padding: 15px 8px;">
            <div style="font-size: 36px; margin-bottom: 8px;">{cards[1]['emoji']}</div>
            <div style="font-size: 13px; color: {colors['accent2']}; margin-bottom: 4px;">{cards[1]['name']}</div>
            <div style="font-size: 10px; color: {colors['text_dim']}; letter-spacing: 1px;">PRESENT</div>
        </div>
        <div style="font-size: 18px; color: {colors['gold']}; padding: 0 5px;">⟡</div>
        <div style="flex: 1; text-align: center; padding: 15px 8px;">
            <div style="font-size: 36px; margin-bottom: 8px;">{cards[2]['emoji']}</div>
            <div style="font-size: 13px; color: {colors['accent3']}; margin-bottom: 4px;">{cards[2]['name']}</div>
            <div style="font-size: 10px; color: {colors['text_dim']}; letter-spacing: 1px;">FUTURE</div>
        </div>
    </div>

    <!-- 分隔线 -->
    <div style="text-align: center; margin-bottom: 20px; color: {colors['gold']}; letter-spacing: 6px; font-size: 10px;">✧ · ˚ ✦ · ˚ ✧</div>

    <!-- 关系分析 -->
    <div style="margin-bottom: 15px; padding: 18px; background: {colors['card_bg']}; border-radius: 12px; border-left: 3px solid {colors['accent1']}; clear: both;">
        <div style="font-size: 11px; color: {colors['accent1']}; letter-spacing: 2px; margin-bottom: 10px; text-transform: uppercase;">✧ Relationship</div>
        <div style="font-size: 13px; color: {colors['text_dim']}; line-height: 1.7;">{rel_analysis}</div>
    </div>

    <!-- 能量流向 -->
    <div style="margin-bottom: 15px; padding: 18px; background: {colors['card_bg']}; border-radius: 12px; border-left: 3px solid {colors['accent2']}; clear: both;">
        <div style="font-size: 11px; color: {colors['accent2']}; letter-spacing: 2px; margin-bottom: 10px; text-transform: uppercase;">⚡ Energy Flow</div>
        <div style="font-size: 12px; color: {colors['text']}; line-height: 1.8;">{energy0}<br>{energy1}<br>{energy2}</div>
    </div>

    <!-- 综合解读 -->
    <div style="margin-bottom: 15px; padding: 18px; background: {colors['card_bg']}; border-radius: 12px; border: 1px solid {colors['gold']}33; clear: both;">
        <div style="font-size: 11px; color: {colors['gold']}; letter-spacing: 2px; margin-bottom: 10px; text-transform: uppercase;">✧ The Reading</div>
        <div style="font-size: 13px; color: {colors['text']}; line-height: 1.8; font-style: italic; white-space: pre-line;">{text}</div>
    </div>

    <!-- 维度分析 -->
    <div style="margin-bottom: 15px; padding: 18px; background: {colors['card_bg']}; border-radius: 12px; border-left: 3px solid {colors['accent3']}; clear: both;">
        <div style="font-size: 11px; color: {colors['accent3']}; letter-spacing: 2px; margin-bottom: 10px; text-transform: uppercase;">🎯 Dimensions</div>
        <div style="font-size: 12px; color: {colors['text_dim']}; line-height: 1.9;">❤️ {love}<br>💼 {work}<br>🏥 {health}<br>💰 {money}</div>
    </div>

    <!-- 行动指南 -->
    <div style="margin-bottom: 15px; padding: 18px; background: {colors['card_bg']}; border-radius: 12px; border-left: 3px solid {colors['gold']}; clear: both;">
        <div style="font-size: 11px; color: {colors['gold']}; letter-spacing: 2px; margin-bottom: 10px; text-transform: uppercase;">💡 Guidance</div>
        <div style="font-size: 12px; color: {colors['text']}; line-height: 1.8;">{action0}<br><br>{action1}<br><br>{action2}</div>
    </div>

    <!-- 底部金句 -->
    <div style="text-align: center; margin-top: 20px; padding: 20px; background: {colors['card_bg']}; border-radius: 16px; border: 1px solid {colors['gold']}44; clear: both;">
        <div style="font-size: 10px; color: {colors['text_dim']}; letter-spacing: 3px; margin-bottom: 12px; text-transform: uppercase;">✧ Today's Wisdom</div>
        <div style="font-size: 14px; color: {colors['gold']}; font-style: italic;">"{cards[2]['goldSentence']}"</div>
        <div style="margin-top: 12px; font-size: 14px; color: {colors['silver']};">🌙 ✦ ☀️</div>
    </div>

</div>"""
    return html