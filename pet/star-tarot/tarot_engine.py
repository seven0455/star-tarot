# -*- coding: utf-8 -*-
from tarot_db import TAROT_DB

def generate_three_card_comprehensive(cards):
    """
    生成三牌阵的深度综合解读（紧凑排版，适配深色主题）
    """
    if len(cards) < 3:
        return "<p>错误：需要三张牌。</p>"

    # 1. 三牌总览
    overview = f"{cards[0]['name']} → {cards[1]['name']} → {cards[2]['name']}"

    # 2. 关系分析
    rel_analysis = f"从「{cards[0]['coreEnergy']}」到「{cards[2]['coreEnergy']}」，{cards[1]['name']}处于转折点。"

    # 3. 能量流向
    energy0 = f"{cards[0]['emoji']} {cards[0]['name']}：{cards[0]['coreEnergy']}。"
    energy1 = f"{cards[1]['emoji']} {cards[1]['name']}：{cards[1]['coreEnergy']}。"
    energy2 = f"{cards[2]['emoji']} {cards[2]['name']}：{cards[2]['coreEnergy']}。"

    # 4. 综合解读
    text = f"""这组牌揭示了从{cards[0]['name']}到{cards[2]['name']}的演化过程。
起始于{cards[0]['summary']}，这是支撑你的能量根源。
目前经历{cards[1]['name']}——{cards[1]['summary']}，这是成长的考验。
未来指向{cards[2]['name']}——{cards[2]['summary']}，预示圆满。"""

    # 5. 维度
    love = f"感情从{cards[0]['name']}的纯真出发，经{cards[1]['name']}的考验，走向{cards[2]['name']}的成熟。"
    work = f"事业：{cards[0]['name']}积累遭遇{cards[1]['name']}的挑战，{cards[2]['name']}预示突破。"
    health = f"健康：调节{cards[1]['name']}带来的压力，重拾{cards[2]['name']}的活力。"
    money = f"财富：从波动转向稳健，{cards[2]['name']}带来丰盛。"

    # 6. 行动
    action0 = f"【接纳{cards[0]['name']}】{cards[0]['guidance'][:80]}..."
    action1 = f"【拥抱{cards[1]['name']}】{cards[1]['guidance'][:80]}..."
    action2 = f"【期待{cards[2]['name']}】{cards[2]['guidance'][:80]}..."

    # 构建紧凑HTML（统一字号，去除多余留白）
    html = f"""
<div style="font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; max-width: 700px; margin: 0 auto; padding: 15px; color: #ccc; line-height: 1.6; font-size: 14px;">

    <!-- 三牌流程 -->
    <div style="display: flex; justify-content: center; align-items: center; gap: 15px; margin-bottom: 20px; padding: 15px;">
        <div style="text-align: center;">
            <div style="font-size: 28px;">{cards[0]['emoji']}</div>
            <div style="font-size: 13px; color: #a78bfa; margin-top: 4px;">{cards[0]['name']}</div>
        </div>
        <div style="color: #666;">→</div>
        <div style="text-align: center;">
            <div style="font-size: 28px;">{cards[1]['emoji']}</div>
            <div style="font-size: 13px; color: #c678dd; margin-top: 4px;">{cards[1]['name']}</div>
        </div>
        <div style="color: #666;">→</div>
        <div style="text-align: center;">
            <div style="font-size: 28px;">{cards[2]['emoji']}</div>
            <div style="font-size: 13px; color: #43e97b; margin-top: 4px;">{cards[2]['name']}</div>
        </div>
    </div>

    <!-- 核心主题 -->
    <div style="text-align: center; margin-bottom: 15px; font-size: 14px; color: #e67e22;">✨ {overview} ✨</div>

    <!-- 关系分析 -->
    <div style="margin-bottom: 12px; font-size: 13px;">
        <div style="color: #a78bfa; margin-bottom: 4px;">🔮 关系</div>
        <div style="color: #999;">{rel_analysis}</div>
    </div>

    <!-- 能量流向 -->
    <div style="margin-bottom: 12px; font-size: 13px;">
        <div style="color: #c678dd; margin-bottom: 6px;">⚡ 能量</div>
        <div style="color: #999; line-height: 1.8;">{energy0}<br>{energy1}<br>{energy2}</div>
    </div>

    <!-- 综合解读 -->
    <div style="margin-bottom: 12px; font-size: 13px;">
        <div style="color: #2980b9; margin-bottom: 6px;">📖 解读</div>
        <div style="color: #bbb; line-height: 1.8;">{text}</div>
    </div>

    <!-- 维度分析 -->
    <div style="margin-bottom: 12px; font-size: 12px; color: #999;">
        <div style="color: #43e97b; margin-bottom: 6px;">🎯 维度</div>
        <div style="line-height: 1.7;">❤️ {love}<br>💼 {work}<br>🏥 {health}<br>💰 {money}</div>
    </div>

    <!-- 行动指南 -->
    <div style="margin-bottom: 12px; font-size: 12px;">
        <div style="color: #e67e22; margin-bottom: 6px;">💡 行动</div>
        <div style="color: #aaa; line-height: 1.8;">{action0}<br><br>{action1}<br><br>{action2}</div>
    </div>

    <!-- 金句 -->
    <div style="text-align: center; margin-top: 15px; padding-top: 15px; border-top: 1px solid #333; font-size: 13px; color: #888; font-style: italic;">"{cards[2]['goldSentence']}"</div>

</div>"""
    return html