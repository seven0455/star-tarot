#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小七星座运势服务器 - 专业版
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import json
import urllib.parse
import os
import random
import time
from datetime import datetime
from collections import OrderedDict

API_KEY = "sk-nykzuklkfjoxyjlindbkxyijjxppdrrjdnonuynemzttlzch"
API_URL = "https://api.siliconflow.cn/v1/chat/completions"
MODEL = "Qwen/Qwen2.5-7B-Instruct"

PET_DIR = r"C:\.openclaw\workspace\pet"

last_request_time = 0
MIN_REQUEST_INTERVAL = 3

response_cache = OrderedDict()
CACHE_TTL = 300
CACHE_MAX_SIZE = 100

# 星座数据知识库 - 详细版
CONSTELLATION_DATA = {
    "白羊座": {
        "symbol": "♈", "dates": "3月21日-4月19日", "element": "火象星座",
        "ruling_planet": "火星",
        "traits": "勇敢、冲动、乐观、自信、领导力强、竞争意识强",
        "personality": "白羊座的人充满活力与热情，像永远年轻的战士。他们 direct、热情、行动派，面对困难从不退缩。天生的领导者，有强烈的竞争意识，喜欢挑战和冒险。",
        "strengths": ["行动力强", "勇敢无畏", "充满激情", "领导能力强", "积极乐观"],
        "weaknesses": ["容易冲动", "缺乏耐心", "自我为中心", "有时过于直接"],
        "career": ["适合创业", "销售", "体育相关", "军事", "急诊医生"],
        "love": ["热情直接", "追求主动", "喜欢挑战", "但可能缺乏细腻"],
        "lucky_colors": ["红色", "橙色", "金色", "白色"],
        "lucky_numbers": [1, 9, 10, 19, 28, 37],
        "compatible": ["狮子座", "射手座", "双子座"],
        "uncompatible": ["巨蟹座", "摩羯座", "天秤座"],
        "health": ["注意头部健康", "小心意外伤害", "保持规律运动"],
        "tips": ["学着放慢脚步", "多倾听他人意见", "避免冲动决策"]
    },
    "金牛座": {
        "symbol": "♉", "dates": "4月20日-5月20日", "element": "土象星座",
        "ruling_planet": "金星",
        "traits": "稳重、务实、固执、有耐心、追求稳定、美食爱好者",
        "personality": "金牛座是十二星座中最踏实的一个，他们稳重务实，追求稳定的生活。对美有天赋，热爱美食和艺术。固执是他们的特点，一旦下定决心就很难改变。",
        "strengths": ["踏实可靠", "有耐心", "艺术气质", "财务观念强", "忠诚可靠"],
        "weaknesses": ["固执", "缺乏变通", "有时过于物质", "节奏慢"],
        "career": ["财务会计", "艺术设计", "美食餐饮", "房地产", "稳定型工作"],
        "love": ["忠诚专一", "浪漫细腻", "但占有欲强", "需要安全感"],
        "lucky_colors": ["绿色", "粉色", "金色", "米色", "淡蓝色"],
        "lucky_numbers": [2, 6, 15, 24, 33, 41],
        "compatible": ["摩羯座", "处女座", "巨蟹座"],
        "uncompatible": ["水瓶座", "天蝎座", "白羊座"],
        "health": ["注意喉咙健康", "新陈代谢较慢", "多做运动"],
        "tips": ["学着接受变化", "别过于执着物质", "勇于尝试新事物"]
    },
    "双子座": {
        "symbol": "♊", "dates": "5月21日-6月21日", "element": "风象星座",
        "ruling_planet": "水星",
        "traits": "灵活、好奇、善变、幽默、沟通能力强、社交达人",
        "personality": "双子座是个充满好奇心的星座，他们像永远长不大的孩子，对一切新事物都感兴趣。聪明伶俐，沟通能力超强，社交圈广泛，但有时缺乏专注力。",
        "strengths": ["聪明机智", "沟通能力强", "适应力强", "多才多艺", "幽默风趣"],
        "weaknesses": ["缺乏专注", "善变", "有时肤浅", "情绪波动大"],
        "career": ["记者", "主播", "销售", "旅游", "教育培训", "社交媒体"],
        "love": ["浪漫有趣", "善于表达", "但可能不够专一", "喜欢新鲜感"],
        "lucky_colors": ["黄色", "银色", "浅蓝色", "橙色"],
        "lucky_numbers": [3, 12, 21, 30, 39, 48],
        "compatible": ["天秤座", "水瓶座", "白羊座"],
        "uncompatible": ["处女座", "双鱼座", "天蝎座"],
        "health": ["注意神经系统", "容易焦虑", "保持规律作息"],
        "tips": ["学会专注", "对感情更认真", "别只是三分钟热度"]
    },
    "巨蟹座": {
        "symbol": "♋", "dates": "6月22日-7月22日", "element": "水象星座",
        "ruling_planet": "月亮",
        "traits": "温柔、体贴、敏感、恋家、第六感强、护短",
        "personality": "巨蟹座是十二星座中最温柔的一个，他们重视家庭和感情，像母亲一样照顾身边的人。敏感而细腻，第六感很强，能感知他人的情绪变化。",
        "strengths": ["温柔体贴", "顾家", "直觉敏锐", "记忆力强", "忠诚可靠"],
        "weaknesses": ["过于敏感", "情绪化", "爱钻牛角尖", "占有欲强"],
        "career": ["医疗护理", "心理咨询", "教育", "餐饮", "母婴相关"],
        "love": ["温柔浪漫", "全心付出", "但容易受伤", "需要被保护"],
        "lucky_colors": ["白色", "银色", "淡蓝色", "淡紫色"],
        "lucky_numbers": [2, 8, 11, 20, 29, 38, 47],
        "compatible": ["天蝎座", "双鱼座", "金牛座"],
        "uncompatible": ["天秤座", "射手座", "白羊座"],
        "health": ["注意肠胃健康", "情绪影响身体", "需要更多安全感"],
        "tips": ["别太敏感", "学着放下过去", "建立自信"]
    },
    "狮子座": {
        "symbol": "♌", "dates": "7月23日-8月22日", "element": "火象星座",
        "ruling_planet": "太阳",
        "traits": "自信、热情、慷慨、领导力、表演欲强、爱面子",
        "personality": "狮子座是天生王者，他们自信满满，热爱成为焦点。慷慨大方，喜欢照顾人，有强大的领导力。但有时过于爱面子，需要不断的赞美和认可。",
        "strengths": ["领导力强", "自信乐观", "慷慨大方", "有创意", "表演天赋"],
        "weaknesses": ["爱面子", "有时傲慢", "需要被关注", "控制欲强"],
        "career": ["管理", "演艺", "公关", "娱乐", "政治", "创意总监"],
        "love": ["浪漫热情", "大方慷慨", "但喜欢被崇拜", "需要很多关注"],
        "lucky_colors": ["金色", "橙色", "黄色", "红色", "黑色"],
        "lucky_numbers": [1, 10, 19, 28, 37, 46],
        "compatible": ["白羊座", "射手座", "双子座"],
        "uncompatible": ["天蝎座", "处女座", "水瓶座"],
        "health": ["注意心脏健康", "背部保养", "避免过度劳累"],
        "tips": ["学会倾听", "别总是要当焦点", "低调一点也挺好"]
    },
    "处女座": {
        "symbol": "♍", "dates": "8月23日-9月22日", "element": "土象星座",
        "ruling_planet": "水星",
        "traits": "完美主义、细心、挑剔、分析力强、有条理、务实",
        "personality": "处女座是十二星座中最追求完美的，他们细致入微，对细节有极高的要求。聪明而有分析能力，做事有条理，但有时过于挑剔和批评。",
        "strengths": ["细心谨慎", "分析能力强", "勤劳可靠", "有条理", "求知欲强"],
        "weaknesses": ["完美主义", "过于挑剔", "爱担心", "有时过于严肃"],
        "career": ["会计", "编辑", "医疗", "科研", "数据分析", "品质管理"],
        "love": ["细腻体贴", "注重细节", "但可能过于挑剔", "需要学会包容"],
        "lucky_colors": ["棕色", "米色", "淡黄色", "灰色", "淡绿色"],
        "lucky_numbers": [5, 14, 23, 32, 41, 50],
        "compatible": ["摩羯座", "金牛座", "巨蟹座"],
        "uncompatible": ["双子座", "射手座", "双鱼座"],
        "health": ["注意肠胃", "神经系统", "容易焦虑"],
        "tips": ["别太追求完美", "学会放松", "对人对己都宽容些"]
    },
    "天秤座": {
        "symbol": "♎", "dates": "9月23日-10月23日", "element": "风象星座",
        "ruling_planet": "金星",
        "traits": "和谐、优雅、公正、犹豫不决、社交能力强、追求美",
        "personality": "天秤座是美的化身，他们优雅，追求和谐。善于社交，人缘好，喜欢公平正义。但决策能力弱，常常犹豫不决。",
        "strengths": ["优雅气质", "社交能力强", "公平正义", "艺术品味", "沟通能力强"],
        "weaknesses": ["犹豫不决", "逃避冲突", "过于在意他人看法", "表面而非实质"],
        "career": ["设计师", "律师", "外交", "公关", "艺术", "音乐"],
        "love": ["浪漫优雅", "重视沟通", "但害怕冲突", "需要陪伴"],
        "lucky_colors": ["粉色", "淡蓝色", "米色", "淡紫色", "白色"],
        "lucky_numbers": [6, 15, 24, 33, 42, 51],
        "compatible": ["双子座", "水瓶座", "狮子座"],
        "uncompatible": ["摩羯座", "天蝎座", "巨蟹座"],
        "health": ["注意腰部", "肾脏健康", "避免久坐"],
        "tips": ["学着做决定", "别总是取悦所有人", "面对冲突不要逃避"]
    },
    "天蝎座": {
        "symbol": "♏", "dates": "10月24日-11月22日", "element": "水象星座",
        "ruling_planet": "冥王星",
        "traits": "神秘、深沉、执着、第六感强、爱恨分明、占有欲强",
        "personality": "天蝎座是十二星座中最神秘的，他们深邃而难以捉摸。第六感极强，能洞察人心。爱恨分明，一旦爱上就全心投入，但占有欲也很强。",
        "strengths": ["洞察力强", "意志坚定", "专注深情", "勇敢", "执行力强"],
        "weaknesses": ["占有欲强", "爱嫉妒", "记仇", "难以信任他人"],
        "career": ["侦探", "心理医生", "研究人员", "商业", "医疗", "金融"],
        "love": ["深情专注", "爱恨分明", "但占有欲强", "需要绝对忠诚"],
        "lucky_colors": ["深红色", "黑色", "深蓝色", "紫色", "暗绿色"],
        "lucky_numbers": [4, 13, 22, 31, 40, 49],
        "compatible": ["巨蟹座", "双鱼座", "处女座"],
        "uncompatible": ["狮子座", "天秤座", "水瓶座"],
        "health": ["注意生殖系统", "新陈代谢", "保持情绪稳定"],
        "tips": ["学会信任", "放下控制欲", "别总是记仇"]
    },
    "射手座": {
        "symbol": "♐", "dates": "11月23日-12月21日", "element": "火象星座",
        "ruling_planet": "木星",
        "traits": "自由、乐观、坦诚、爱冒险、幽默、正直",
        "personality": "射手座是十二星座中最热爱自由的，他们像一匹野马，向往诗和远方。乐观积极，爱开玩笑，直觉敏锐，善于社交。",
        "strengths": ["乐观开朗", "爱冒险", "正直诚实", "幽默感强", "适应力强"],
        "weaknesses": ["缺乏耐心", "过于直接", "承诺难兑现", "有时粗心"],
        "career": ["旅游", "教育", "销售", "体育", "媒体", "自由职业"],
        "love": ["浪漫热情", "轻松有趣", "但害怕束缚", "需要空间"],
        "lucky_colors": ["紫色", "蓝色", "浅绿色", "棕色", "粉红色"],
        "lucky_numbers": [3, 12, 21, 30, 39, 48],
        "compatible": ["白羊座", "狮子座", "水瓶座"],
        "uncompatible": ["处女座", "天蝎座", "金牛座"],
        "health": ["注意肝脏", "大腿", "臀部", "避免过度消耗"],
        "tips": ["学会承诺", "别总是逃避", "对感情认真一点"]
    },
    "摩羯座": {
        "symbol": "♑", "dates": "12月22日-1月19日", "element": "土象星座",
        "ruling_planet": "土星",
        "traits": "务实、稳重、有责任感、耐心、野心、保守",
        "personality": "摩羯座是十二星座中最有责任感的，他们像登山者，一步一步往上爬。务实而有耐心，为了目标可以牺牲享受。意志坚强，但有时过于严肃。",
        "strengths": ["责任感强", "务实可靠", "有耐心", "意志坚强", "自律"],
        "weaknesses": ["过于严肃", "缺乏情趣", "悲观", "控制欲强"],
        "career": ["管理", "金融", "法律", "政治", "建筑", "科研"],
        "love": ["专一忠诚", "默默付出", "但表达含蓄", "需要时间打开心扉"],
        "lucky_colors": ["灰色", "棕色", "黑色", "深蓝色", "绿色"],
        "lucky_numbers": [4, 8, 13, 22, 31, 40],
        "compatible": ["金牛座", "处女座", "天蝎座"],
        "uncompatible": ["天秤座", "白羊座", "射手座"],
        "health": ["注意骨骼", "关节", "皮肤", "注意保暖"],
        "tips": ["学着放松", "表达情感", "别总是压抑自己"]
    },
    "水瓶座": {
        "symbol": "♒", "dates": "1月20日-2月18日", "element": "风象星座",
        "ruling_planet": "天王星",
        "traits": "独立、创新、博爱、人道主义、理性、固执",
        "personality": "水瓶座是十二星座中最独特的，他们像来自未来的使者。独立思考，追求创新，重视人道主义。但有时候过于理性，难以理解他人情感。",
        "strengths": ["创新能力", "独立思考", "人道精神", "理性客观", "博爱"],
        "weaknesses": ["过于理性", "难以捉摸", "固执", "不近人情"],
        "career": ["科学家", "发明家", "社会活动", "公益", "IT", "航空"],
        "love": ["灵魂伴侣", "重视精神", "但保持距离", "需要空间"],
        "lucky_colors": ["天蓝色", "银色", "彩虹色", "黑色", "粉红色"],
        "lucky_numbers": [7, 16, 25, 34, 43, 52],
        "compatible": ["天秤座", "双子座", "射手座"],
        "uncompatible": ["金牛座", "天蝎座", "处女座"],
        "health": ["注意小腿", "血液循环", "神经系统"],
        "tips": ["关注情感", "别太冷漠", "学会融入社群"]
    },
    "双鱼座": {
        "symbol": "♓", "dates": "2月19日-3月20日", "element": "水象星座",
        "ruling_planet": "海王星",
        "traits": "浪漫、敏感、艺术性强、同理心、逃避现实、迷糊",
        "personality": "双鱼座是十二星座中最梦幻的，他们像水中的鱼，自由而敏感。富有艺术气质，感知力超强，能感受他人的痛苦与快乐。但有时候逃避现实，活在自己的梦里。",
        "strengths": ["艺术天赋", "感知力强", "善解人意", "浪漫", "直觉强"],
        "weaknesses": ["逃避现实", "容易受伤", "缺乏界限", "有时不切实际"],
        "career": ["艺术", "音乐", "电影", "心理咨询", "医疗", "慈善"],
        "love": ["浪漫深情", "全身心投入", "但容易受伤", "需要被保护"],
        "lucky_colors": ["海蓝色", "绿色", "紫色", "白色", "淡粉色"],
        "lucky_numbers": [2, 11, 20, 29, 38, 47],
        "compatible": ["巨蟹座", "天蝎座", "金牛座"],
        "uncompatible": ["狮子座", "射手座", "双子座"],
        "health": ["注意脚", "免疫系统", "容易疲劳"],
        "tips": ["学着面对现实", "建立界限", "别总是逃避"]
    }
}

def get_cache(key):
    if key in response_cache:
        item = response_cache[key]
        if time.time() - item['time'] < CACHE_TTL:
            return item['response']
        else:
            del response_cache[key]
    return None

def set_cache(key, response):
    response_cache[key] = {'response': response, 'time': time.time()}
    if len(response_cache) > CACHE_MAX_SIZE:
        response_cache.popitem(last=False)

def generate_professional_fortune(constellation_name, fortune_type="all"):
    """生成专业运势报告"""
    data = CONSTELLATION_DATA.get(constellation_name)
    if not data:
        return None
    
    today = datetime.now().strftime("%Y年%m月%d日")
    seed = hash(today + constellation_name)
    random.seed(seed)
    
    # 运势等级
    love_score = random.randint(70, 98)
    career_score = random.randint(70, 98)
    health_score = random.randint(70, 98)
    wealth_score = random.randint(70, 98)
    
    def score_to_star(score):
        stars = int(score / 20)
        return "★" * stars + "☆" * (5 - stars)
    
    # 详细运势
    love_descriptions = [
        f"今日爱情运势{score_to_star(love_score)}，单身者有机会遇到心动的对象，建议多参加社交活动。",
        f"今日桃花运{score_to_star(love_score)}，有伴侣者感情稳定，单身者可能会有意外邂逅。",
        f"今日感情运势{score_to_star(love_score)}，适合约会、表白，但要注意沟通方式。"
    ]
    
    career_descriptions = [
        f"事业运势{score_to_star(career_score)}，工作中可能遇到新的机会，适合展现能力。",
        f"今日职场运势{score_to_star(career_score)}，贵人运不错，适合寻求合作或指导。",
        f"事业运势{score_to_star(career_score)}，直觉敏锐，适合做决策或谈判。"
    ]
    
    health_descriptions = [
        f"健康运势{score_to_star(health_score)}，精力充沛，但注意不要过度消耗。",
        f"今日健康运势{score_to_star(health_score)}，身心状态不错，适合运动或户外活动。",
        f"健康运势{score_to_star(health_score)}，需要关注情绪健康，保持心情愉悦。"
    ]
    
    wealth_descriptions = [
        f"财运{score_to_star(wealth_score)}，可能有意外收入或奖金，注意理财。",
        f"今日财运{score_to_star(wealth_score)}，适合投资或理财，但避免冒险。",
        f"财运{score_to_star(wealth_score)}，花钱要谨慎，但也有贵人相助带来财机会。"
    ]
    
    # 生成报告
    result = f"""
✨ {data['symbol']} {constellation_name} ({data['dates']})
📅 {today}
🌟 守护星：{data['ruling_planet']} | 🌍 元素：{data['element']}

━━━━━━━━━━━━━━━━━━━━
📊 今日综合运势评分
━━━━━━━━━━━━━━━━━━━━
💕 爱情: {score_to_star(love_score)} ({love_score}%)
💼 事业: {score_to_star(career_score)} ({career_score}%)
💪 健康: {score_to_star(health_score)} ({health_score}%)
💰 财运: {score_to_star(wealth_score)} ({wealth_score}%)

━━━━━━━━━━━━━━━━━━━━
💝 今日运势详解
━━━━━━━━━━━━━━━━━━━━

【爱情运势】{random.choice(love_descriptions)}

【事业运势】{random.choice(career_descriptions)}

【健康运势】{random.choice(health_descriptions)}

【财富运势】{random.choice(wealth_descriptions)}

━━━━━━━━━━━━━━━━━━━━
🍀 今日幸运提示
━━━━━━━━━━━━━━━━━━━━
🎨 幸运色：{random.choice(data['lucky_colors'])}
🔢 幸运数：{random.choice(data['lucky_numbers'])}
👤 贵人星座：{random.choice(data['compatible'])}
⚠️ 注意星座：{random.choice(data['uncompatible'])}

━━━━━━━━━━━━━━━━━━━━
💡 今日小贴士
━━━━━━━━━━━━━━━━━━━━
{data['tips'][0]}

━━━━━━━━━━━━━━━━━━━━
🌙 性格特点
━━━━━━━━━━━━━━━━━━━━
{data['personality']}

优势：{', '.join(data['strengths'][:3])}
需要注意：{', '.join(data['weaknesses'][:2])}
"""
    return result

def chat_with_minimax(message):
    global last_request_time
    
    cache_key = message.strip()
    cached = get_cache(cache_key)
    if cached:
        return cached
    
    now = time.time()
    elapsed = now - last_request_time
    if elapsed < MIN_REQUEST_INTERVAL:
        time.sleep(MIN_REQUEST_INTERVAL - elapsed)
    
    last_request_time = time.time()
    
    # 检查星座
    constellation = None
    for name in CONSTELLATION_DATA.keys():
        if name in message:
            constellation = name
            break
    
    fortune = generate_professional_fortune(constellation) if constellation else None
    
    system_prompt = """你是一个专业的星座运势分析师，名叫小七（🐼）。
你结合了陶白白的诗意风格和专业的数据分析能力。

【回复格式要求】

一、开场（诗意）
- 用1-2句诗意的语言概括今日特点，或一个画面感的场景
-参考陶白白风格："今天的你像一杯温热的拿铁，香气四溢但需要慢慢品味"

二、核心数据（详细）
必须包含以下具体数据：
- 💕 爱情指数：XX%（用具体数字）
- 💼 事业指数：XX%
- 💰 财运指数：XX%
- 💪 健康指数：XX%
- ⭐ 今日综合评分：XX/100

三、分析解读（深度）
- 结合数据，分析每个方面的运势
- 用陶白白风格的语言，诗意但有深度
- 说出灵魂深处的特点，不只是表面

四、金句（陶白白风格）
- 1-2句总结性的话，让人印象深刻
- 参考："白羊座的勇敢不是不怕，是在怕的时候还能向前走"

五、今日提示（实用）
- 行动建议：适合做什么/不适合做什么
- 幸运颜色+数字+贵人星座

【记住】
- 数据要具体，不要模糊
- 诗意和实用都要有
- 像一个懂星座又懂人心的朋友在跟你聊天"""
    
    if fortune:
        system_prompt += f"\n\n【星座数据】\n{fortune}"
    else:
        system_prompt += """
你是小七星座馆的星座分析师，可以回答用户关于星座的问题。
支持的星座：白羊座、金牛座、双子座、巨蟹座、狮子座、处女座、天秤座、天蝎座、射手座、摩羯座、水瓶座、双鱼座
可以提供性格分析、运势查询、配对建议等服务。"""
    
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        "max_tokens": 800,
        "temperature": 0.8
    }
    
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(data).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
    )
    
    try:
        r = urllib.request.urlopen(req, timeout=30)
        resp = json.loads(r.read().decode('utf-8'))
        if 'choices' in resp and len(resp['choices']) > 0:
            result = resp['choices'][0]['message']['content']
            set_cache(cache_key, result)
            return result
    except Exception as e:
        return f"抱歉，小七休息一下: {e}"
    
    return "小七没收到回复呢..."

class ChatHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html' or self.path == '/chat.html':
            html_file = os.path.join(PET_DIR, 'chat.html')
            try:
                with open(html_file, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(content)
            except:
                self.send_error(404, 'Not Found')
        elif self.path == '/avatar_2.png':
            png_file = r"C:\.openclaw\workspace\avatar_2.png"
            try:
                with open(png_file, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'image/png')
                self.end_headers()
                self.wfile.write(content)
            except:
                self.send_error(404, 'Not Found')
        else:
            self.send_error(404, 'Not Found')
    
    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            
            message = params.get('message', [''])[0]
            
            if message:
                reply = chat_with_minimax(message)
            else:
                reply = "小七没收到消息呢..."
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps({'reply': reply}, ensure_ascii=False)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_error(404)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8090), ChatHandler)
    print("小七星座运势服务器(专业版)启动成功！")
    print("访问: http://localhost:8090")
    print("外网: http://12lh2886154tq.vicp.fun")
    server.serve_forever()
