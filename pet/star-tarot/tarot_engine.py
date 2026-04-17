# -*- coding: utf-8 -*-
from tarot_db import TAROT_DB

def generate_three_card_comprehensive(cards):
    """
    生成三牌阵的深度综合解读（简洁文本格式）
    """
    if len(cards) < 3:
        return "<p>错误：需要三张牌进行综合解读。</p>"

    # 1. 三牌总览
    overview = f"从{cards[0]['name']}到{cards[2]['name']}的旅程"
    if len(overview) > 20:
        overview = f"{cards[0]['name']} → {cards[1]['name']} → {cards[2]['name']}"

    # 2. 关系分析
    rel_narrative = f"{cards[0]['name']}（过去）→ {cards[1]['name']}（现在）→ {cards[2]['name']}（未来）"
    rel_analysis = f"这三张牌构成了一个从「{cards[0]['coreEnergy']}」到「{cards[2]['coreEnergy']}」的转化路径。目前的{cards[1]['name']}正处于转折的关键点。"

    # 3. 能量流向深度分析
    energy_flow = f"""【起点 · {cards[0]['name']}】
{cards[0]['emoji']} {cards[0]['coreEnergy']}
{cards[0]['summary']}

【过程 · {cards[1]['name']}】
{cards[1]['emoji']} {cards[1]['coreEnergy']}
{cards[1]['summary']}

【终点 · {cards[2]['name']}】
{cards[2]['emoji']} {cards[2]['coreEnergy']}
{cards[2]['summary']}"""

    flow_summary = f"能量从{cards[0]['suit']}流向{cards[2]['suit']}，预示着一段深刻的自我转化。"

    # 4. 三牌综合解读
    comprehensive_text = f"""这组牌面揭示了一个深刻的能量演化过程。

起始于{cards[0]['name']}——{cards[0]['summary']}。这代表了您过去所拥有的基础或初衷，是支撑您走到今天的能量根源。

然而，目前您正经历着{cards[1]['name']}的洗礼——{cards[1]['summary']}。这不仅仅是一个障碍，更是灵魂在向更高层次跨越前的必要考验。{cards[1]['goldSentence']}

这种转变是必要的，因为未来的{cards[2]['name']}正带着「{cards[2]['summary']}」的能量向您走来。{cards[2]['goldSentence']}"""

    # 5. 维度分析
    dimensions = f"""【爱情】{cards[0]['name']}带来的纯真回忆正在滋养您，当前{cards[1]['name']}的考验会让感情更加成熟，最终走向{cards[2]['name']}的圆满。

【事业】过去的积累（{cards[0]['name']}）正遭遇当前的挑战（{cards[1]['name']}），但请坚持，{cards[2]['name']}预示着突破性的成功。

【健康】注意心理健康的调节，从{cards[1]['name']}的焦虑中释放，找回生命的活力。

【财富】财务能量正在经历转化，从波动的阶段转向稳健丰盛的收获期。"""

    # 6. 行动指南
    actions = f"""【接纳{cards[0]['name']}】
{cards[0]['guidance'][:100]}...
思考：这份来自过去的能量如何支持你？

【拥抱{cards[1]['name']}】
{cards[1]['guidance'][:100]}...
行动：今天如何主动参与这个转化过程？

【期待{cards[2]['name']}】
{cards[2]['guidance'][:100]}...
态度：保持开放，相信最好的还在前方。"""

    # 构建简洁的纯文本 HTML（无复杂样式，确保兼容性）
    html_content = f"""
<div style="font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; line-height: 1.8;">

    <!-- 三牌流程 -->
    <div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin-bottom: 25px; padding: 25px; background: #f8f9fa; border-radius: 12px;">
        <div style="text-align: center;">
            <div style="font-size: 2.5em; margin-bottom: 5px;">{cards[0]['emoji']}</div>
            <div style="font-weight: bold; color: #333;">{cards[0]['name']}</div>
            <div style="font-size: 0.85em; color: #666;">过去</div>
        </div>
        <div style="font-size: 1.8em; color: #666;">→</div>
        <div style="text-align: center;">
            <div style="font-size: 2.5em; margin-bottom: 5px;">{cards[1]['emoji']}</div>
            <div style="font-weight: bold; color: #333;">{cards[1]['name']}</div>
            <div style="font-size: 0.85em; color: #666;">现在</div>
        </div>
        <div style="font-size: 1.8em; color: #666;">→</div>
        <div style="text-align: center;">
            <div style="font-size: 2.5em; margin-bottom: 5px;">{cards[2]['emoji']}</div>
            <div style="font-weight: bold; color: #333;">{cards[2]['name']}</div>
            <div style="font-size: 0.85em; color: #666;">未来</div>
        </div>
    </div>

    <!-- 核心主题 -->
    <div style="text-align: center; margin-bottom: 25px; padding: 18px; background: #f8f9fa; border-radius: 12px;">
        <div style="font-size: 1.3em; color: #333; font-weight: bold;">{overview}</div>
    </div>

    <!-- 关系分析 -->
    <div style="margin-bottom: 20px; padding: 18px; background: #fff; border-radius: 10px; border: 1px solid #ddd;">
        <div style="font-weight: bold; color: #333; margin-bottom: 10px; font-size: 1.1em;">关系分析</div>
        <div style="color: #555; margin-bottom: 8px;">{rel_narrative}</div>
        <div style="color: #444; line-height: 1.7;">{rel_analysis}</div>
    </div>

    <!-- 能量流向 -->
    <div style="margin-bottom: 20px; padding: 18px; background: #fff; border-radius: 10px; border: 1px solid #ddd;">
        <div style="font-weight: bold; color: #333; margin-bottom: 12px; font-size: 1.1em;">能量流向分析</div>
        <div style="line-height: 2; color: #444; font-size: 0.95em;">{energy_flow}</div>
        <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #eee; color: #555; font-size: 0.9em;">{flow_summary}</div>
    </div>

    <!-- 三牌综合解读 -->
    <div style="margin-bottom: 20px; padding: 20px; background: #fff; border-radius: 10px; border: 1px solid #ddd;">
        <div style="font-weight: bold; color: #333; margin-bottom: 15px; font-size: 1.1em;">三牌综合解读</div>
        <div style="line-height: 2; color: #333; font-size: 0.95em; white-space: pre-line;">{comprehensive_text}</div>
    </div>

    <!-- 维度分析 -->
    <div style="margin-bottom: 20px; padding: 18px; background: #fff; border-radius: 10px; border: 1px solid #ddd;">
        <div style="font-weight: bold; color: #333; margin-bottom: 12px; font-size: 1.1em;">维度分析</div>
        <div style="line-height: 2; color: #444; font-size: 0.9em; white-space: pre-line;">{dimensions}</div>
    </div>

    <!-- 行动指南 -->
    <div style="margin-bottom: 20px; padding: 18px; background: #fff; border-radius: 10px; border: 1px solid #ddd;">
        <div style="font-weight: bold; color: #333; margin-bottom: 12px; font-size: 1.1em;">行动指南</div>
        <div style="line-height: 2; color: #444; font-size: 0.9em; white-space: pre-line;">{actions}</div>
    </div>

    <!-- 金句 -->
    <div style="text-align: center; padding: 20px; background: #f8f9fa; border-radius: 10px;">
        <div style="font-size: 1.05em; color: #333; font-style: italic;">"{cards[2]['goldSentence']}"</div>
    </div>

</div>"""
    return html_content