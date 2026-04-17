# -*- coding: utf-8 -*-
from tarot_db import TAROT_DB

def generate_three_card_comprehensive(cards):
    """
    生成三牌阵的深度综合解读（HTML格式）
    
    参数:
    cards: 包含3张牌数据的列表，每张牌是一个字典，包含 name, emoji, suit, keywords, summary, coreEnergy, guidance, goldSentence
    """
    if len(cards) < 3:
        return "<p>错误：需要三张牌进行综合解读。</p>"

    # 1. 三牌总览 (20字内)
    # 尝试根据核心能量提取关键词生成总览
    overview = f"从{cards[0]['name']}的启示到{cards[2]['name']}的圆满。"
    if len(overview) > 20:
        overview = f"{cards[0]['name']} -> {cards[1]['name']} -> {cards[2]['name']}"

    # 2. 关系分析
    rel_narrative = f"{cards[0]['name']}（过去）→ {cards[1]['name']}（现在）→ {cards[2]['name']}（未来）"
    rel_analysis = f"这三张牌构成了一个从“{cards[0]['coreEnergy']}”到“{cards[2]['coreEnergy']}”的转化路径。目前的{cards[1]['name']}正处于转折的关键点。"

    # 3. 能量流向深度分析
    energy_flow = [
        f"<li><strong>起点（{cards[0]['name']}）：</strong>{cards[0]['coreEnergy']}。这是您当前处境的根源。</li>",
        f"<li><strong>过程（{cards[1]['name']}）：</strong>{cards[1]['coreEnergy']}。这是您正在经历的挑战或状态。</li>",
        f"<li><strong>终点（{cards[2]['name']}）：</strong>{cards[2]['coreEnergy']}。这是能量最终汇聚的方向。</li>"
    ]
    flow_summary = f"能量从{cards[0]['suit']}的波动流向{cards[2]['suit']}的稳定，预示着一段深刻的自我转化过程。"

    # 4. 三牌综合解读 (200-300字)
    # 综合 guidance 生成一段更有深度的叙事
    intro = f"这组牌面揭示了一个深刻的能量演化过程。起始于{cards[0]['name']}的“{cards[0]['summary']}”，这代表了您过去所拥有的基础或初衷。"
    challenge = f"然而，目前您正经历着{cards[1]['name']}的洗礼。{cards[1]['summary']}。这不仅仅是一个障碍，更是灵魂在向更高层次跨越前的必要考验。正如牌面所揭示的：{cards[1]['goldSentence']}"
    transformation = f"这种痛苦或停滞是暂时的，因为未来的{cards[2]['name']}正带着“{cards[2]['summary']}”的能量向您走来。这预示着一切努力终将获得圆满。"
    advice = f"在行动上，{cards[0]['guidance'][:60]}... 这种来自过去的治愈力量是您现在的解药。而面对未来的{cards[2]['name']}，请记住：{cards[2]['goldSentence']}。保持觉知，黎明就在眼前。"
    
    comprehensive_text = f"{intro} {challenge} {transformation} {advice}"

    # 5. 维度分析
    dimensions = {
        "爱情": f"在感情中，经历了{cards[0]['name']}的纯真，正面临{cards[1]['name']}的考验，最终将走向{cards[2]['name']}的圆满。",
        "事业": f"事业上，过去的积累（{cards[0]['name']}）正遭遇当前的瓶颈（{cards[1]['name']}），但只要坚持，{cards[2]['name']}预示着巨大的成功。",
        "健康": f"注意心理压力的调节，从{cards[1]['name']}的焦虑中释放，找回{cards[2]['name']}的活力。",
        "财富": f"财务状况正从波动的阶段转向更加稳健和丰盛的未来。"
    }

    # 6. 行动指南
    actions = [
        f"回顾并汲取{cards[0]['name']}中的积极能量，将其转化为动力。",
        f"正视{cards[1]['name']}带来的挑战，不要逃避，寻找突破口。",
        f"保持对{cards[2]['name']}所代表目标的信心，坚定地执行当前计划。"
    ]

    # 构建 HTML 内容
    html_content = f"""
    <div class="tarot-reading">
        <style>
            .tarot-reading {{
                font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
                color: #2c3e50;
                line-height: 1.6;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .section {{
                margin-bottom: 25px;
                padding: 15px;
                background: white;
                border-radius: 8px;
                border-left: 5px solid #3498db;
            }}
            .section-title {{
                font-size: 1.2em;
                font-weight: bold;
                color: #2980b9;
                margin-bottom: 10px;
                display: flex;
                align-items: center;
            }}
            .overview {{
                font-size: 1.4em;
                text-align: center;
                color: #e67e22;
                margin-bottom: 20px;
                font-weight: bold;
            }}
            .card-flow {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 20px;
                text-align: center;
            }}
            .card-item {{
                flex: 1;
                padding: 10px;
            }}
            .card-emoji {{ font-size: 2em; }}
            .card-name {{ font-weight: bold; margin-top: 5px; }}
            .dimension-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
            }}
            .dimension-item {{
                padding: 10px;
                background: #ecf0f1;
                border-radius: 4px;
            }}
            .action-list {{
                padding-left: 20px;
            }}
            .gold-sentence {{
                font-style: italic;
                color: #7f8c8d;
                text-align: center;
                margin-top: 10px;
                font-size: 0.9em;
            }}
        </style>

        <div class="overview">✨ {overview} ✨</div>

        <div class="card-flow">
            <div class="card-item">
                <div class="card-emoji">{cards[0]['emoji']}</div>
                <div class="card-name">{cards[0]['name']}</div>
                <div style="font-size: 0.8em; color: #95a5a6;">过去</div>
            </div>
            <div class="card-item" style="display: flex; align-items: center; justify-content: center;">➡️</div>
            <div class="card-item">
                <div class="card-emoji">{cards[1]['emoji']}</div>
                <div class="card-name">{cards[1]['name']}</div>
                <div style="font-size: 0.8em; color: #95a5a6;">现在</div>
            </div>
            <div class="card-item" style="display: flex; align-items: center; justify-content: center;">➡️</div>
            <div class="card-item">
                <div class="card-emoji">{cards[2]['emoji']}</div>
                <div class="card-name">{cards[2]['name']}</div>
                <div style="font-size: 0.8em; color: #95a5a6;">未来</div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">1. 三牌总览</div>
            <p>{overview}</p>
        </div>

        <div class="section">
            <div class="section-title">2. 关系分析</div>
            <p><strong>路径：</strong>{rel_narrative}</p>
            <p>{rel_analysis}</p>
        </div>

        <div class="section">
            <div class="section-title">3. 能量流向深度分析</div>
            <ul style="padding-left: 20px;">
                {"".join(energy_flow)}
            </ul>
            <p style="margin-top: 10px; border-top: 1px dashed #ddd; padding-top: 10px;">
                <strong>小结：</strong>{flow_summary}
            </p>
        </div>

        <div class="section">
            <div class="section-title">4. 三牌综合解读</div>
            <p>{comprehensive_text}</p>
        </div>

        <div class="section">
            <div class="section-title">5. 维度分析</div>
            <div class="dimension-grid">
                <div class="dimension-item"><strong>❤️ 爱情：</strong>{dimensions['爱情']}</div>
                <div class="dimension-item"><strong>💼 事业：</strong>{dimensions['事业']}</div>
                <div class="dimension-item"><strong>🏥 健康：</strong>{dimensions['健康']}</div>
                <div class="dimension-item"><strong>💰 财富：</strong>{dimensions['财富']}</div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">6. 行动指南</div>
            <ul class="action-list">
                {"".join([f"<li>{a}</li>" for a in actions])}
            </ul>
        </div>

        <div class="gold-sentence">
            “{cards[2]['goldSentence']}”
        </div>
    </div>
    """
    return html_content
