// 塔罗牌完整数据 - 78张牌（深度解读版）
// 小七深度整理 | 不是知识的堆砌，是智慧的传递
// 最后更新：2026-04-17

const tarotDeck = {
    // 大阿尔卡纳 (22张)
    majorArcana: [
        {
            id: 0, name: '愚人 The Fool', emoji: '🃏',
            keywords: ['新的开始', '无限可能', '冒险', '天真', '流浪'],
            summary: '一张象征无限可能的白纸，今天适合踏出第一步',
            coreEnergy: '纯粹的冒险精神和beginner\'s mind',
            guidance: `🌊 【关于愚人，你要知道的事】

愚人不是"傻"，而是"空"。

一个装满水的杯子不能再装新茶，一个背负太多过去的人不能再轻盈出发。

【今天你会遇到的】
你可能会遇到一个选择：安稳地留在原地，还是踏出未知的一步？

【小七的解读】
问问自己：是什么让你犹豫了？是现实的风险，还是内心的恐惧？

牌面在说：如果你一直想做的事还没做，今天可能是那个"对的时刻"。

不是因为准备好了才出发，而是出发了才会真正准备好。

【今日课题】
放下"万一失败怎么办"的思考，改为问自己："如果我不敢，这个遗憾会跟多久？"

⚠️ 但也别盲目，今天的冒险需要基本的判断力。不是每个悬崖都值得跳。`,
            love: { score: 4, content: '单身：今天可能会遇到让你心动的人。不是因为对方多完美，而是某个瞬间击中了你。有伴：关系中的"新鲜感"需要主动创造。', tip: '与其想"他/她是不是对的人"，不如问自己"我有没有在关系里做真实的自己？"' },
            career: { score: 3, content: '今天你可能会遇到一个新机会或新想法。', tip: '记录下你今天冒出的想法' },
            health: { score: 4, content: '身体今天特别轻盈，适合户外活动。', tip: '如果可以，走一条不熟悉的路回家' },
            wealth: { score: 3, content: '财务上可能有新的想法或机会出现。', tip: '可以了解新事物，但不要急于投资' },
            luckyNumber: '21', luckyColor: '黄色', luckyDirection: '东方',
            goldSentence: '不是因为准备好了才出发，而是出发了才会真正准备好。',
            reversedMeaning: '逆位的愚人可能是：太冲动或太害怕。找到自己的平衡点。'
        },
        {
            id: 1, name: '魔术师 The Magician', emoji: '🪄',
            keywords: ['创造', '意志力', '技能', '显化', '行动'],
            summary: '你拥有一切所需的资源和能力，今天是行动的日子',
            coreEnergy: '将梦想转化为现实的创造力',
            guidance: `🎩 【关于魔术师，你要知道的事】

魔术师是愚人的下一步：愚人敢于出发，魔术师知道怎么到达。

牌面上的人一只手指天，一只指向地——上接宇宙，下连物质。

【今天你会遇到的】
今天你可能突然意识到：原来我可以做到。

【今日课题】
把手边的一件事从"想"变成"做"。哪怕只是一步。`,
            love: { score: 5, content: '单身：今天你有独特的魅力。做你自己就好。有伴：和伴侣一起"创造"些什么。', tip: '关系需要经营' },
            career: { score: 5, content: '工作运势极强！今天适合展示你的专业能力。', tip: '把一个想法变成具体的行动计划' },
            health: { score: 4, content: '精力充沛，身体状态很好。', tip: '身体是你最重要的工具，投资它' },
            wealth: { score: 4, content: '财务上有好运。今天适合谈判。', tip: '主动争取你应得的' },
            luckyNumber: '1', luckyColor: '红色', luckyDirection: '东方',
            goldSentence: '所有的工具都已经在你手中，现在只需要行动。',
            reversedMeaning: '逆位的魔术师可能意味着：技能没有用在正确的地方。'
        },
        {
            id: 2, name: '女祭司 The High Priestess', emoji: '📜',
            keywords: ['直觉', '神秘', '内在智慧', '子宫', '秘密'],
            summary: '今天适合向内看，倾听内心的声音',
            coreEnergy: '潜意识的智慧和内在指引',
            guidance: `🌙 【关于女祭司，你要知道的事】

女祭司坐在两根柱子之间——一根黑，一根白。她不是在选择，而是在等待。

【今天你会遇到的】
今天你可能会听到一些"奇怪的声音"——可能是直觉，可能是灵感。

【今日课题】
找一个安静的地方，问自己一个问题，然后安静等待。`,
            love: { score: 3, content: '单身：今天桃花运一般，但适合思考自己真正想要什么样的感情。有伴：今天可能更容易理解伴侣深层的需求。', tip: '少说话，多倾听对方没说出的话' },
            career: { score: 3, content: '工作上今天适合思考、规划，而不是执行。', tip: '今天学到的最重要的一课是什么？' },
            health: { score: 4, content: '今天适合冥想、瑜伽等放松活动。', tip: '睡前花10分钟静心' },
            wealth: { score: 2, content: '财务上今天宜静不宜动。', tip: '记录下你对金钱的真实感受' },
            luckyNumber: '2', luckyColor: '蓝色', luckyDirection: '北方',
            goldSentence: '答案一直都在你心里。静下来，听它说。',
            reversedMeaning: '逆位的女祭司可能意味着：你忽略了内心的声音。'
        },
        {
            id: 3, name: '女皇 The Empress', emoji: '👑',
            keywords: ['丰盛', '创造力', '母性', '温暖', '自然'],
            summary: '今天是充满滋养和富足的一天',
            coreEnergy: '丰盛的创造力与滋养的能量',
            guidance: `💐 【关于女皇，你要知道的事】

女皇是大地的母亲。她不是给予者，而是滋养者——像大地一样，让万物自然生长。

【今日课题】
做一件让自己感觉"被爱"的事。不是别人爱你，而是你爱你自己。`,
            love: { score: 5, content: '单身：今天你可能会遇到让你心动的人，好好打扮自己。有伴：今天感情甜蜜日，适合约会。', tip: '告诉对方你爱他/她' },
            career: { score: 4, content: '工作上会有好事发生。', tip: '在工作中展现你温柔但有力的那一面' },
            health: { score: 5, content: '身体状态很好，感觉充满活力。', tip: '给自己做一顿饭' },
            wealth: { score: 4, content: '财务上有好运，可能有额外收入或收到礼物。', tip: '花点钱投资在自己的成长上' },
            luckyNumber: '3', luckyColor: '绿色', luckyDirection: '东方',
            goldSentence: '你值得被爱，不需要任何理由。',
            reversedMeaning: '逆位的女皇可能意味着：过度付出导致自己空了。'
        },
        {
            id: 4, name: '皇帝 The Emperor', emoji: '⚔️',
            keywords: ['权威', '秩序', '结构', '领导力', '父亲'],
            summary: '今天需要你拿出决断力和组织能力',
            coreEnergy: '结构化的力量和理性的领导',
            guidance: `👑 【关于皇帝，你要知道的事】

皇帝是秩序的建立者。他不是发明家，而是组织者——把混沌变成秩序。

【今日课题】
今天适合处理那些你一直拖延的"麻烦事"。不是不做，是找到正确的方式做。`,
            love: { score: 3, content: '单身：今天你对感情的态度比较理性。有伴：今天适合处理关系中实际的问题。', tip: '少一点情绪，多一点行动' },
            career: { score: 5, content: '工作运势极强！你有领导力，能做决定。', tip: '主动承担一点责任' },
            health: { score: 3, content: '注意劳逸结合。', tip: '设定工作和休息的界限' },
            wealth: { score: 4, content: '财务上今天适合做预算、理财规划。', tip: '检查一下你的财务计划是否需要更新' },
            luckyNumber: '4', luckyColor: '金色', luckyDirection: '西方',
            goldSentence: '规则是自由的框架，不是自由的敌人。',
            reversedMeaning: '逆位的皇帝可能意味着：太强硬或太松散。'
        },
        {
            id: 5, name: '教皇 The Hierophant', emoji: '🛐',
            keywords: ['传统', '指导', '精神教诲', '信仰', '道德'],
            summary: '今天是汲取智慧、尊重传统的日子',
            coreEnergy: '精神指引与传统智慧',
            guidance: `🛐 【关于教皇，你要知道的事】

教皇是精神导师。他不是告诉你答案，而是指引你找到自己的答案。

【今日课题】
今天适合学习、读书，或者向有经验的人请教。`,
            love: { score: 3, content: '单身：今天可能通过学习或社交活动遇到志同道合的人。有伴：可能需要一起参加一些有意义的活动。', tip: '和伴侣聊聊你们的价值观是否一致' },
            career: { score: 3, content: '工作上今天适合参加培训、学习新技能。', tip: '找一个 mentor 或教练' },
            health: { score: 3, content: '身体状态稳定。传统养生方法今天特别适合你。', tip: '试试太极、瑜伽等经典运动' },
            wealth: { score: 3, content: '财务上今天适合稳健投资。', tip: '遵循经过验证的理财原则' },
            luckyNumber: '5', luckyColor: '红色', luckyDirection: '东方',
            goldSentence: '智慧来自于传承，也来自于实践。',
            reversedMeaning: '过于叛逆或被错误的教导误导。'
        },
        {
            id: 6, name: '恋人 The Lovers', emoji: '💕',
            keywords: ['爱情', '选择', '结合', '价值观', '沟通'],
            summary: '今天在人际关系上有美好的可能',
            coreEnergy: '连接、选择与价值观的整合',
            guidance: `💕 【关于恋人，你要知道的事】

恋人牌不是只有爱情——它是关于"选择"的牌。

【今日课题】
找一个重要的问题，问自己：哪个选择更接近我想成为的人？`,
            love: { score: 5, content: '单身：今天桃花运极强！有伴：今天适合和伴侣深度沟通。', tip: '坦诚表达你的感受，即使害怕' },
            career: { score: 3, content: '工作上可能需要做选择。听从你的价值观。', tip: '选择让你心动的工作机会' },
            health: { score: 3, content: '身体状态稳定。注意过敏或皮肤问题。', tip: '今天身体感觉可能比较敏感' },
            wealth: { score: 3, content: '财务上今天可能有合作机会。签约前要仔细考虑。', tip: '合作关系要谨慎选择' },
            luckyNumber: '6', luckyColor: '粉红色', luckyDirection: '东方',
            goldSentence: '选择不是问"哪个更好"，而是问"哪个更像我自己"。',
            reversedMeaning: '沟通不畅或价值观冲突。'
        },
        {
            id: 7, name: '战车 The Chariot', emoji: '🏛️',
            keywords: ['胜利', '意志力', '决心', '控制', '前进'],
            summary: '今天的你战无不胜，只要保持坚定的意志',
            coreEnergy: '克服障碍的决心和行动力',
            guidance: `🏆 【关于战车，你要知道的事】

战车是征服者的牌。他不是没有遇到阻碍，而是即使遇到也要前进。

【今日课题】
找一个你一直想做但觉得"太难了"的事，今天开始做。`,
            love: { score: 4, content: '单身：今天你的魅力值很高，适合主动出击。有伴：可能会有点小争执，但最终会和解。', tip: '温柔地坚持' },
            career: { score: 5, content: '工作上会有关卡，但你会克服它。', tip: '坚持就是胜利' },
            health: { score: 4, content: '体力充沛，适合运动竞技。', tip: '把竞争转向自我超越' },
            wealth: { score: 4, content: '财务上有好运，可能有偏财运。', tip: '相信你的直觉' },
            luckyNumber: '7', luckyColor: '银色', luckyDirection: '西方',
            goldSentence: '胜利属于那些即使跌倒也要继续前行的人。',
            reversedMeaning: '失去方向或过于冲动。'
        },
        {
            id: 8, name: '力量 Strength', emoji: '🦁',
            keywords: ['勇气', '耐心', '内在力量', '温柔', '韧性'],
            summary: '今天需要你拿出内在的勇气和耐心',
            coreEnergy: '柔软的力量和内在的勇气',
            guidance: `💪 【关于力量，你要知道的事】

力量牌不是要你变得更强大，而是要你发现：真正的力量不是征服，是转化。

【今日课题】
找一个你一直在逃避的问题。今天面对它。`,
            love: { score: 4, content: '单身：今天适合展现你脆弱的一面。有伴：感情中需要耐心，温柔比强硬更有效。', tip: '用爱融化障碍' },
            career: { score: 3, content: '工作上可能需要耐心等待。', tip: '耐心地坚持下去' },
            health: { score: 5, content: '身体状态不错，适合做一些舒缓的运动。', tip: '倾听身体的信号' },
            wealth: { score: 3, content: '财务上保持稳定。', tip: '稳健理财' },
            luckyNumber: '8', luckyColor: '橙色', luckyDirection: '东方',
            goldSentence: '真正的强大不是征服别人，而是战胜自己。',
            reversedMeaning: '内心恐惧或用蛮力解决问题。'
        },
        {
            id: 9, name: '隐者 The Hermit', emoji: '🏔️',
            keywords: ['内省', '孤独', '寻找真理', '指引', '独处'],
            summary: '今天适合独处和反思，向内寻找答案',
            coreEnergy: '内在的指引与独处的智慧',
            guidance: `🔦 【关于隐者，你要知道的事】

隐者不是逃避者，他是去寻找的人——在黑暗中寻找内心的光。

【今日课题】
给自己1-2小时的独处时间。不是刷手机，是真正一个人待着。`,
            love: { score: 2, content: '单身：今天可能想一个人待着。有伴：今天需要一些独处时间。', tip: '告诉伴侣你需要空间' },
            career: { score: 3, content: '工作上今天适合独自思考、规划。', tip: '把思考的结论写下来' },
            health: { score: 4, content: '今天适合休息和恢复。', tip: '早睡，给身体充分的休息' },
            wealth: { score: 3, content: '财务上今天宜静不宜动。', tip: '规划未来' },
            luckyNumber: '9', luckyColor: '灰色', luckyDirection: '任何方向',
            goldSentence: '有时候，迷路是为了找到真正的自己。',
            reversedMeaning: '孤独感或逃避现实。'
        },
        {
            id: 10, name: '命运之轮 Wheel of Fortune', emoji: '🎡',
            keywords: ['命运', '循环', '转变', '运气', '周期'],
            summary: '今天运势正在转动，保持开放和平衡',
            coreEnergy: '生命周期的转动与意外的转变',
            guidance: `🎡 【关于命运之轮，你要知道的事】

命运之轮在转动——没有永远的坏运，也没有永远的好运。

【今日课题】
接受今天可能发生的变化。不是被动接受，是主动适应。`,
            love: { score: 4, content: '单身：可能有意外的邂逅。有伴：感情可能有转机。', tip: '接受感情的意外发展' },
            career: { score: 3, content: '工作上可能有变动。', tip: '拥抱变化' },
            health: { score: 3, content: '今天身体状态有波动。', tip: '保持平衡' },
            wealth: { score: 5, content: '财务上可能有意外的好运！', tip: '乘胜追击' },
            luckyNumber: '10', luckyColor: '紫色', luckyDirection: '任何方向',
            goldSentence: '生活就像轮子起起落落，接受它，享受它。',
            reversedMeaning: '抗拒变化或运气不佳。'
        },
        {
            id: 11, name: '正义 Justice', emoji: '⚖️',
            keywords: ['公正', '平衡', '因果', '真理', '法律'],
            summary: '今天需要你做公正的决定，承担后果',
            coreEnergy: '因果法则与公正的平衡',
            guidance: `⚖️ 【关于正义，你要知道的事】

正义拿着剑和天平。她说：每个行为都有后果，每个选择都有代价。

【今日课题】
做一个公正的决定，不要偏私。`,
            love: { score: 3, content: '单身：今天在感情上要公正客观。', tip: '诚实地面对自己的感情需求' },
            career: { score: 4, content: '工作上今天适合处理合同、法律或财务问题。', tip: '公正地处理冲突' },
            health: { score: 3, content: '注意肾脏和腰部。', tip: '正确的坐姿' },
            wealth: { score: 4, content: '财务上今天适合处理账目、税务等问题。', tip: '账目要清晰' },
            luckyNumber: '11', luckyColor: '蓝绿色', luckyDirection: '西方',
            goldSentence: '每一个选择都有后果，种什么因得什么果。',
            reversedMeaning: '不公正或逃避责任。'
        },
        {
            id: 12, name: '倒吊人 The Hanged Man', emoji: '🙃',
            keywords: ['等待', '悬而未决', '换一个角度看问题', '牺牲', '暂停'],
            summary: '今天需要你换一个角度看待问题',
            coreEnergy: '视角转换与自愿的暂停',
            guidance: `🙃 【关于倒吊人，你要知道的事】

倒吊人不是被困住，而是主动选择换一个角度看世界。

【今日课题】
找一个你一直在纠结的问题。把自己倒过来（或者转个椅子），再想想。`,
            love: { score: 3, content: '单身：今天感情可能停滞不前。有伴：换个方式沟通。', tip: '倒过来看你们的感情' },
            career: { score: 2, content: '工作上今天进展缓慢。', tip: '休息一下再回来' },
            health: { score: 3, content: '身体上可能感觉有些疲惫。', tip: '躺平一下也没关系' },
            wealth: { score: 2, content: '财务上今天不宜做重大决策。', tip: '观望' },
            luckyNumber: '12', luckyColor: '靛蓝色', luckyDirection: '北方',
            goldSentence: '换一个视角，世界可能会完全不同。',
            reversedMeaning: '不愿意放下或僵持在困境中。'
        },
        {
            id: 13, name: '死神 Death', emoji: '🦋',
            keywords: ['结束', '转变', '新生', '告别', '释放'],
            summary: '放下过去才能迎接新生',
            coreEnergy: '结束与重生的转化',
            guidance: `🦋 【关于死神，你要知道的事】

死神不是字面上的死亡，而是"结束"。

【今日课题】
找一个你可以放下的东西。不需要扔掉，是放下对它的执念。`,
            love: { score: 3, content: '可能有旧爱回来，但今天更适合告别。', tip: '放手才能遇见新的可能' },
            career: { score: 4, content: '工作上可能有项目结束或角色转变。', tip: '拥抱结束' },
            health: { score: 3, content: '身体上可能在排毒，注意休息。', tip: '给自己时间适应' },
            wealth: { score: 3, content: '财务上可能需要止损。', tip: '断舍离' },
            luckyNumber: '13', luckyColor: '黑色', luckyDirection: '西方',
            goldSentence: '死亡不是终点，而是新生的开始。',
            reversedMeaning: '抗拒改变或沉溺于过去。'
        },
        {
            id: 14, name: '节制 Temperance', emoji: '🌈',
            keywords: ['平衡', '调和', '中庸之道', '耐心', '净化'],
            summary: '今天需要找到平衡点',
            coreEnergy: '平衡、调和与中庸之道',
            guidance: `🌈 【关于节制，你要知道的事】

节制不是禁欲，是找到"刚刚好"。

【今日课题】
找一个你一直在走极端的事。试着找到"刚刚好"的平衡点。`,
            love: { score: 4, content: '单身：今天在感情上比较理性。有伴：今天适合调和矛盾。', tip: '中庸之道' },
            career: { score: 3, content: '工作上需要平衡不同的任务。', tip: '多样化' },
            health: { score: 4, content: '身体上需要平衡饮食和运动。', tip: '平衡是关键' },
            wealth: { score: 3, content: '财务上需要平衡收入和支出。', tip: '适度就好' },
            luckyNumber: '14', luckyColor: '彩虹色', luckyDirection: '南方',
            goldSentence: '平衡不是妥协，而是智慧。',
            reversedMeaning: '失衡或过度放纵。'
        },
        {
            id: 15, name: '恶魔 The Devil', emoji: '⛓️',
            keywords: ['束缚', '欲望', '物质主义', '执念', '陷阱'],
            summary: '今天要小心被欲望或执念束缚',
            coreEnergy: '束缚与执念的挑战',
            guidance: `⛓️ 【关于恶魔，你要知道的事】

恶魔不是外界的恶，是内心的枷锁。

【今日课题】
找一个你一直被它控制的事。今天开始减少对它的依赖。`,
            love: { score: 2, content: '感情上可能有执念或嫉妒。', tip: '自由地爱' },
            career: { score: 3, content: '工作上可能有诱惑让你走捷径。', tip: '不要被利益诱惑' },
            health: { score: 2, content: '身体上可能有放纵的倾向。', tip: '适度享受' },
            wealth: { score: 3, content: '财务上可能有诱惑想赚快钱。', tip: '稳健为主' },
            luckyNumber: '15', luckyColor: '深红色', luckyDirection: '南方',
            goldSentence: '认识到自己的弱点，才是改变的第一步。',
            reversedMeaning: '正在挣脱束缚，是积极的转变信号！'
        },
        {
            id: 16, name: '塔 The Tower', emoji: '⚡',
            keywords: ['突变', '破坏', '觉醒', '灾难', '解放'],
            summary: '今天可能会有意外变化，但这是破茧前的阵痛',
            coreEnergy: '突如其来的转变与觉醒',
            guidance: `⚡ 【关于塔，你要知道的事】

塔是被雷电击中的建筑——不是惩罚，是解放。

【今日课题】
如果今天有意外的变化，记住：这是旧的结束，新的开始。`,
            love: { score: 2, content: '感情上可能有突然的冲突或变化。', tip: '风暴中保持冷静' },
            career: { score: 3, content: '工作上可能有意外变动。', tip: '准备好备份计划' },
            health: { score: 2, content: '注意意外伤害。', tip: '安全第一' },
            wealth: { score: 2, content: '财务上可能有意外支出。', tip: '量入为出' },
            luckyNumber: '16', luckyColor: '白色', luckyDirection: '任何方向',
            goldSentence: '有时候破坏是重建的开始。',
            reversedMeaning: '变革会以更温和的方式发生。'
        },
        {
            id: 17, name: '星星 The Star', emoji: '✨',
            keywords: ['希望', '灵感', '宁静', '疗愈', '愿景'],
            summary: '今天会有一道光照进你的生命',
            coreEnergy: '希望、疗愈与灵感的能量',
            guidance: `✨ 【关于星星，你要知道的事】

星星是在暴风雨后出现的。它说：最黑暗的时刻已经过去。

【今日课题】
找一个你一直在纠结的伤痛。今天开始放下，或者开始疗愈。`,
            love: { score: 5, content: '单身：今天桃花运不错。有伴：感情疗愈中，适合和伴侣重新开始。', tip: '给感情一个新的开始' },
            career: { score: 4, content: '工作上会有灵感迸发。', tip: '描绘你的理想' },
            health: { score: 5, content: '身心都在恢复期。', tip: '让自己休息和恢复' },
            wealth: { score: 4, content: '财务上运气不错。', tip: '充满希望地规划' },
            luckyNumber: '17', luckyColor: '浅蓝色', luckyDirection: '东方',
            goldSentence: '即使在最黑暗的夜晚，星星也会为你指引方向。',
            reversedMeaning: '失去方向或抑郁消沉。但这只是暂时的。'
        },
        {
            id: 18, name: '月亮 The Moon', emoji: '🌙',
            keywords: ['幻觉', '恐惧', '潜意识', '不安', '迷茫'],
            summary: '今天要小心迷雾，分清真实和幻觉',
            coreEnergy: '潜意识的活动与直觉的迷雾',
            guidance: `🌙 【关于月亮，你要知道的事】

月亮照亮夜晚，但也会制造阴影。我们看到的东西不一定是真实的。

【今日课题】
找一个你一直在害怕的事。今天面对它，而不是被它控制。`,
            love: { score: 2, content: '今天可能在感情上有些不安全感。', tip: '不要疑神疑鬼' },
            career: { score: 2, content: '工作上可能有误导信息。', tip: '眼见不一定为实' },
            health: { score: 3, content: '情绪波动可能影响睡眠。', tip: '睡前不要看手机' },
            wealth: { score: 2, content: '财务上可能有欺骗或误导。', tip: '谨慎投资' },
            luckyNumber: '18', luckyColor: '银色', luckyDirection: '西方',
            goldSentence: '面对恐惧时，闭上眼睛深呼吸，问问自己真正害怕的是什么。',
            reversedMeaning: '迷惑和恐惧正在消散。'
        },
        {
            id: 19, name: '太阳 The Sun', emoji: '☀️',
            keywords: ['快乐', '活力', '成功', '活力', '生命力'],
            summary: '今天是超级幸运日！',
            coreEnergy: '生命力，成功与纯粹的快乐',
            guidance: `☀️ 【关于太阳，你要知道的事】

太阳是最纯粹的光。今天一切都会顺利！

【今日课题】
今天适合做任何事。面试、谈判、约会、表白——都会顺利！`,
            love: { score: 5, content: '单身：今天魅力四射，桃花运爆棚！有伴：感情甜蜜幸福！', tip: '享受爱' },
            career: { score: 5, content: '工作运超强！今天适合做任何事。', tip: '趁热打铁' },
            health: { score: 5, content: '精力充沛，身体状态极佳！', tip: '释放你的活力' },
            wealth: { score: 5, content: '财运大旺！可能有意外之财。', tip: '抓住机会' },
            luckyNumber: '19', luckyColor: '金色', luckyDirection: '东方',
            goldSentence: '太阳底下无新事，但每一天都是新的开始。',
            reversedMeaning: '小成功、喜悦减半。但整体仍是好日子。'
        },
        {
            id: 20, name: '审判 Judgement', emoji: '📯',
            keywords: ['重生的召唤', '审判', '觉醒', '回顾', '更新'],
            summary: '今天适合回顾过去，做出改变',
            coreEnergy: '觉醒、回顾与重生的召唤',
            guidance: `📯 【关于审判，你要知道的事】

审判号角响起，旧的我被召唤回来接受审判。不是为了惩罚，是为了整合。

【今日课题】
找一个你一直在后悔的事。今天换个角度看待它。`,
            love: { score: 4, content: '可能会收到前任的消息。', tip: '放下过去' },
            career: { score: 4, content: '工作上可能有一个复盘的机会。', tip: '从经验中学习' },
            health: { score: 3, content: '身体上可能提醒你需要改变一些习惯。', tip: '开始新的健康计划' },
            wealth: { score: 4, content: '财务上适合评估过去的投资决策。', tip: '重新规划' },
            luckyNumber: '20', luckyColor: '白色', luckyDirection: '东方',
            goldSentence: '是时候放下过去，拥抱真正属于你的未来了。',
            reversedMeaning: '自我怀疑或后悔过去。'
        },
        {
            id: 21, name: '世界 The World', emoji: '🌍',
            keywords: ['完成', '成就感', '圆满', '整合', '成就'],
            summary: '今天是一个阶段的圆满完成',
            coreEnergy: '完成、成就与圆满的整合',
            guidance: `🌍 【关于世界，你要知道的事】

世界是一张圆满的牌。你已经走了很远，现在是一个重大周期的结束。

【今日课题】
回顾一下你这一路走来的历程。不是为了证明什么，是为了感谢自己。`,
            love: { score: 5, content: '可能结束单身生活，或者感情进入新的阶段。', tip: '感恩现在的伴侣' },
            career: { score: 5, content: '工作上可能完成一个重大项目。', tip: '犒劳自己' },
            health: { score: 4, content: '身体状态达到一个平衡。', tip: '感谢身体' },
            wealth: { score: 5, content: '财务上可能有一个圆满的结果。', tip: '分享你的财富' },
            luckyNumber: '21', luckyColor: '金色', luckyDirection: '任何方向',
            goldSentence: '每件事的结束都是新开始的序曲。',
            reversedMeaning: '目标未达成或缺乏成就感。'
        }
    ],

    // ==================== 小阿尔卡纳 (56张) ====================
    // 权杖牌组 (Wands) - 火元素 - 创造力、激情、行动
    wands: [
        {
            id: 'wands-ace', name: '权杖王牌 Ace of Wands', emoji: '🔥',
            suit: '权杖', suitElement: '火',
            keywords: ['新的开始', '创造力', '灵感', '潜力', '热情'],
            summary: '一个新的创意或行动机会正在萌芽',
            coreEnergy: '创造的原始动力，灵感之火的点燃',
            guidance: `🔥 【关于权杖Ace】

这是宇宙在你心中点燃的一簇火焰。

【今日课题】
今天有没有一件你一直想尝试的事？哪怕只是发一条消息、做一个小的改变，都是在给火焰添柴。`,
            love: { score: 4, content: '单身：可能会有新的浪漫机会。有伴：感情中注入新鲜活力。', tip: '表达你的感情' },
            career: { score: 5, content: '可能会有新项目或新机会。', tip: '大胆尝试' },
            health: { score: 4, content: '精力充沛，适合开始新的运动计划。', tip: '燃烧你的卡路里' },
            wealth: { score: 4, content: '可能有新的赚钱想法。', tip: '把握机会' },
            luckyNumber: '1', luckyColor: '红色', luckyDirection: '东方',
            goldSentence: '火焰已经点燃，让它燃烧吧。',
            reversedMeaning: '创意被阻碍或缺乏动力。'
        },
        {
            id: 'wands-2', name: '权杖二 Two of Wands', emoji: '🏰',
            suit: '权杖', suitElement: '火',
            keywords: ['计划', '决策', '可能性', '选择', '探索'],
            summary: '站在分岔路口，面前有多条路可以选择',
            coreEnergy: '在探索中寻找自己的道路',
            guidance: `🏰 【关于权杖二】

画面中的人站在城墙上，手握权杖，眺望着远方。他在想：我应该往左走，还是往右走？

【今日课题】
写下你现在面临的选择，然后列出每个选择的"最坏结果"和"最好结果"。`,
            love: { score: 3, content: '可能面临感情的选择。', tip: '跟随你的心' },
            career: { score: 4, content: '职业规划或转换的时机。', tip: '做明智的选择' },
            health: { score: 3, content: '适合做健康计划的决定。', tip: '长远考虑' },
            wealth: { score: 3, content: '投资或财务方向的选择。', tip: '谨慎规划' },
            luckyNumber: '2', luckyColor: '橙色', luckyDirection: '西方',
            goldSentence: '选择没有对错，只有选择后的诠释。',
            reversedMeaning: '犹豫不决或缺乏方向。'
        },
        {
            id: 'wands-3', name: '权杖三 Three of Wands', emoji: '⛵',
            suit: '权杖', suitElement: '火',
            keywords: ['等待', '远见', '扩张', '海外', '商机'],
            summary: '你的船已经出发，现在是在海上等待风来',
            coreEnergy: '播种后的耐心守望',
            guidance: `⛵ 【关于权杖三】

船已经下水了。航海者站在山顶，看着他的三艘船驶向远方。

【今日课题】
想想你正在等待的一件事。今天与其焦虑，不如做点小事让它更接近目标。`,
            love: { score: 4, content: '异地恋或海外缘分。', tip: '耐心等待' },
            career: { score: 4, content: '项目进展中，需要耐心。', tip: '持续努力' },
            health: { score: 3, content: '保持现状，等待时机。', tip: '不要急躁' },
            wealth: { score: 4, content: '投资收益需要时间。', tip: '静待佳音' },
            luckyNumber: '3', luckyColor: '黄色', luckyDirection: '东方',
            goldSentence: '船已下水，风会来的。',
            reversedMeaning: '等待过久或缺乏进展。'
        },
        {
            id: 'wands-4', name: '权杖四 Four of Wands', emoji: '🎊',
            suit: '权杖', suitElement: '火',
            keywords: ['庆祝', '稳定', '和谐', '欢庆', '家园'],
            summary: '该停下来庆祝一下了，你值得被祝贺',
            coreEnergy: '在成就中感受简单的快乐',
            guidance: `🎊 【关于权杖四】

花环已经挂好，庆典已经准备好。这是一个"停下来，闻闻玫瑰花"的时刻。

【今日课题】
今天找一件值得庆祝的小事，然后真的去庆祝。`,
            love: { score: 5, content: '适合约会或庆祝感情中的好事。', tip: '享受两人时光' },
            career: { score: 5, content: '工作上的成就要庆祝！', tip: '团队建设' },
            health: { score: 4, content: '身心状态和谐。', tip: '保持好的状态' },
            wealth: { score: 4, content: '财务上有好消息。', tip: '犒劳自己' },
            luckyNumber: '4', luckyColor: '绿色', luckyDirection: '东方',
            goldSentence: '快乐是一种能力，不是一种结果。',
            reversedMeaning: '不稳定的庆祝或冲突。'
        },
        {
            id: 'wands-5', name: '权杖五 Five of Wands', emoji: '⚔️',
            suit: '权杖', suitElement: '火',
            keywords: ['冲突', '竞争', '挑战', '混乱', '多样性'],
            summary: '周围很乱，但这种混乱里有活力',
            coreEnergy: '在竞争中找到自己的位置',
            guidance: `⚔️ 【关于权杖五】

五个人在混战，每个人都挥舞着权杖。但仔细看——没有人真的在伤害谁。

【今日课题】
如果今天遇到冲突，问自己：我的立场是什么？我是想赢，还是想找到最好的解决方案？`,
            love: { score: 2, content: '可能会有竞争或争执。', tip: '保持冷静' },
            career: { score: 3, content: '工作中有竞争。', tip: '以和为贵' },
            health: { score: 3, content: '压力增大，注意休息。', tip: '避免冲突' },
            wealth: { score: 3, content: '有竞争但也有机会。', tip: '脱颖而出' },
            luckyNumber: '5', luckyColor: '红色', luckyDirection: '南方',
            goldSentence: '竞争要优雅，输了也不失风度。',
            reversedMeaning: '避免冲突或失败的竞争。'
        },
        {
            id: 'wands-6', name: '权杖六 Six of Wands', emoji: '🏆',
            suit: '权杖', suitElement: '火',
            keywords: ['胜利', '认可', '成功', '荣誉', '骄傲'],
            summary: '你的努力被看见了，你走在胜利的路上',
            coreEnergy: '被认可的喜悦和自信',
            guidance: `🏆 【关于权杖六】

英雄骑着白马回来了，周围的人在欢呼。

【今日课题】
今天如果有人表扬你，不要谦虚地说"哪里哪里"。就说一声"谢谢"。`,
            love: { score: 5, content: '感情上得到认可或表扬。', tip: '享受被爱的感觉' },
            career: { score: 5, content: '事业上的成功得到认可！', tip: '再接再厉' },
            health: { score: 4, content: '自信带来更好的状态。', tip: '保持自信' },
            wealth: { score: 5, content: '财务上有好消息。', tip: '庆祝一下' },
            luckyNumber: '6', luckyColor: '金色', luckyDirection: '东方',
            goldSentence: '你配得上这个荣耀。',
            reversedMeaning: '骄傲自满或失败。'
        },
        {
            id: 'wands-7', name: '权杖七 Seven of Wands', emoji: '🛡️',
            suit: '权杖', suitElement: '火',
            keywords: ['防御', '坚持', '勇气', '挑战', '自信'],
            summary: '有人质疑你，但你依然站稳脚跟',
            coreEnergy: '在压力中保持立场',
            guidance: `🛡️ 【关于权杖七】

一个人站在高处，手持权杖，抵御着下方来犯者的挑战。

【今日课题】
如果今天有人质疑你，先不要急着反驳。听听他们在说什么。`,
            love: { score: 3, content: '感情中需要坚持自己。', tip: '守护你的感情' },
            career: { score: 4, content: '职场挑战需要勇气面对。', tip: '不要退缩' },
            health: { score: 3, content: '需要守护你的健康边界。', tip: '学会说不' },
            wealth: { score: 3, content: '财务上需要守护。', tip: '谨慎管理' },
            luckyNumber: '7', luckyColor: '红色', luckyDirection: '西方',
            goldSentence: '防御是为了保护，不是为了树敌。',
            reversedMeaning: '感到被压迫或放弃抵抗。'
        },
        {
            id: 'wands-8', name: '权杖八 Eight of Wands', emoji: '💨',
            suit: '权杖', suitElement: '火',
            keywords: ['速度', '行动', '进展', '移动', '好消息'],
            summary: '事情开始快速推进，一切都动起来了',
            coreEnergy: '顺势而动的流动与速度',
            guidance: `💨 【关于权杖八】

八根权杖在空中快速飞行。这是一个"开弓没有回头箭"的时刻。

【今日课题】
今天有没有一件拖了很久的事？给自己10分钟，先做了再说。`,
            love: { score: 4, content: '感情快速进展。', tip: '跟上节奏' },
            career: { score: 5, content: '工作快速推进！', tip: '把握时机' },
            health: { score: 4, content: '活力充沛。', tip: '动起来' },
            wealth: { score: 4, content: '财务消息快速传来。', tip: '快速响应' },
            luckyNumber: '8', luckyColor: '橙色', luckyDirection: '东方',
            goldSentence: '该快的时候就快。',
            reversedMeaning: '延迟或阻碍。'
        },
        {
            id: 'wands-9', name: '权杖九 Nine of Wands', emoji: '🏰',
            suit: '权杖', suitElement: '火',
            keywords: ['韧性', '坚持', '经验', '谨慎', '守护'],
            summary: '你已经很累了，但终点就在眼前',
            coreEnergy: '在疲惫中坚守到最后',
            guidance: `🏰 【关于权杖九】

一个人守在城堡中，身上伤痕累累，但仍然紧握权杖，警惕地望着远方。

【今日课题】
今天照顾好自己。疲惫的时候，一杯热茶比一顿烧烤更治愈。`,
            love: { score: 3, content: '感情中需要坚持。', tip: '曙光就在前方' },
            career: { score: 3, content: '最后冲刺阶段。', tip: '再坚持一下' },
            health: { score: 2, content: '注意休息，你累了。', tip: '照顾好自己' },
            wealth: { score: 3, content: '财务上需要守护。', tip: '保持警惕' },
            luckyNumber: '9', luckyColor: '棕色', luckyDirection: '西方',
            goldSentence: '能坚持到现在，你已经很了不起了。',
            reversedMeaning: '疲惫过度或准备放弃。'
        },
        {
            id: 'wands-10', name: '权杖十 Ten of Wands', emoji: '🏋️',
            suit: '权杖', suitElement: '火',
            keywords: ['负担', '责任', '压力', '辛劳', '到达目的地'],
            summary: '你扛着太多了，是时候放下一些',
            coreEnergy: '放下不必要的重负',
            guidance: `🏋️ 【关于权杖十】

一个人背着十根权杖，弯腰前行。他已经快到目的地了，但负重让他喘不过气。

【今日课题】
列一个清单：你现在在扛哪些不需要自己扛的东西？`,
            love: { score: 2, content: '压力过大影响感情。', tip: '减压' },
            career: { score: 2, content: '工作压力过大。', tip: '学会委托' },
            health: { score: 2, content: '压力影响健康。', tip: '必须休息' },
            wealth: { score: 2, content: '财务负担重。', tip: '精简生活' },
            luckyNumber: '10', luckyColor: '棕色', luckyDirection: '东方',
            goldSentence: '懂得放下的人，才是真正有力量的人。',
            reversedMeaning: '无法放下或负担过重。'
        },
        {
            id: 'wands-page', name: '权杖侍从 Page of Wands', emoji: '📜',
            suit: '权杖', suitElement: '火',
            keywords: ['探索', '发现', '自由', '独立', '热忱'],
            summary: '带着好奇心出发，世界等着你去发现',
            coreEnergy: '年轻而充满可能性的探索精神',
            guidance: `📜 【关于权杖侍从】

一个年轻的使者手持权杖，眺望远方。

【今日课题】
今天有没有一件事是你一直想学的？哪怕是"了解一点点"，今天就开始吧。`,
            love: { score: 4, content: '新的浪漫可能即将出现。', tip: '保持开放' },
            career: { score: 4, content: '学习新技能的好时机。', tip: '探索新领域' },
            health: { score: 4, content: '充满活力。', tip: '尝试新运动' },
            wealth: { score: 3, content: '新的财务机会。', tip: '关注新项目' },
            luckyNumber: '11', luckyColor: '黄色', luckyDirection: '东方',
            goldSentence: '年轻的心不需要理由，只需要热情。',
            reversedMeaning: '缺乏方向或热情减退。'
        },
        {
            id: 'wands-knight', name: '权杖骑士 Knight of Wands', emoji: '🐴',
            suit: '权杖', suitElement: '火',
            keywords: ['行动', '冲动', '热情', '勇敢', '冒险'],
            summary: '带着火焰般的热情冲向前方',
            coreEnergy: '充满行动力的冲刺',
            guidance: `🐴 【关于权杖骑士】

骑士骑着马，带着火焰冲向远方。

【今日课题】
今天如果有人催你，先问自己：我是因为害怕，还是因为真的想？`,
            love: { score: 4, content: '热情追求。', tip: '勇敢表达' },
            career: { score: 4, content: '快速行动。', tip: '不要犹豫' },
            health: { score: 4, content: '精力充沛。', tip: '释放能量' },
            wealth: { score: 4, content: '抓住机会。', tip: '冲动但乐观' },
            luckyNumber: '12', luckyColor: '红色', luckyDirection: '南方',
            goldSentence: '行动力是天赋，但方向比速度更重要。',
            reversedMeaning: '冲动或行动缺乏方向。'
        },
        {
            id: 'wands-queen', name: '权杖皇后 Queen of Wands', emoji: '👑',
            suit: '权杖', suitElement: '火',
            keywords: ['自信', '领导力', '热情', '创造力', '勇气'],
            summary: '你是自己世界里的女王，有能量照亮所有人',
            coreEnergy: '温暖而坚定的女性力量',
            guidance: `👑 【关于权杖皇后】

皇后坐在她的宝座上，狮子安静地蹲在脚边。她自信，但不咄咄逼人。

【今日课题】
今天你可以主动承担一件小事。不是为了证明什么，是因为你本来就可以。`,
            love: { score: 5, content: '充满魅力。', tip: '展现真实的你' },
            career: { score: 5, content: '领导力展现。', tip: '带领团队' },
            health: { score: 4, content: '状态极佳。', tip: '保持活力' },
            wealth: { score: 4, content: '财务上有好运。', tip: '自信决策' },
            luckyNumber: '13', luckyColor: '橙色', luckyDirection: '东方',
            goldSentence: '领导力不是控制，是服务。',
            reversedMeaning: '自私或缺乏自信。'
        },
        {
            id: 'wands-king', name: '权杖国王 King of Wands', emoji: '🗡️',
            suit: '权杖', suitElement: '火',
            keywords: ['领导', '决断', '愿景', '成就感', '权威'],
            summary: '你有能力创造和领导，让愿景变为现实',
            coreEnergy: '成熟而果断的领导力',
            guidance: `🗡️ 【关于权杖国王】

国王手持权杖，坐在宝座上，目光坚定，俯瞰着他的王国。

【今日课题】
今天如果你要做一个决定，记住：信息收集完了，决定就已经做好了。`,
            love: { score: 4, content: '需要果断行动。', tip: '领导感情' },
            career: { score: 5, content: '领导力被认可！', tip: '做决定' },
            health: { score: 4, content: '状态良好。', tip: '维持好习惯' },
            wealth: { score: 5, content: '财务决策带来好运。', tip: '大胆投资' },
            luckyNumber: '14', luckyColor: '红色', luckyDirection: '西方',
            goldSentence: '决断力是领导力的核心。',
            reversedMeaning: '过于专制或决策失误。'
        }
    ],

    // 圣杯牌组 (Cups) - 水元素 - 情感、关系、爱、直觉
    cups: [
        {
            id: 'cups-ace', name: '圣杯王牌 Ace of Cups', emoji: '💗',
            suit: '圣杯', suitElement: '水',
            keywords: ['新的感情', '爱', '灵感', '灵性', '机会'],
            summary: '心中的爱开始涌出，像是杯子第一次被倒满',
            coreEnergy: '纯真的爱的开始',
            guidance: `💗 【关于圣杯Ace】

水从圣杯中溢出，流入周围的湖泊。爱在这里是满溢的，不是枯竭的。

【今日课题】
今天对一个人表达感谢，不需要理由，不需要回报。`,
            love: { score: 5, content: '新的爱情萌芽！', tip: '敞开心扉' },
            career: { score: 4, content: '团队关系和谐。', tip: '培养合作' },
            health: { score: 4, content: '情感状态良好。', tip: '爱自己' },
            wealth: { score: 3, content: '内心富足。', tip: '精神大于物质' },
            luckyNumber: '1', luckyColor: '粉红色', luckyDirection: '西方',
            goldSentence: '给予爱不是失去爱，是让爱流动。',
            reversedMeaning: '情感封闭或空虚。'
        },
        {
            id: 'cups-2', name: '圣杯二 Two of Cups', emoji: '💑',
            suit: '圣杯', suitElement: '水',
            keywords: [' partnership', '团结', '吸引力', '爱情', '契合'],
            summary: '两个人的相遇，像是水流汇入同一片海',
            coreEnergy: '关系的建立与深化',
            guidance: `💑 【关于圣杯二】

两个人各持一个圣杯，水在两者之间流动，形成一个完整的循环。

【今日课题】
今天找一个人，好好聊聊天。`,
            love: { score: 5, content: '浪漫关系或合作伙伴。', tip: '共同成长' },
            career: { score: 4, content: '合作关系顺利。', tip: '互利共赢' },
            health: { score: 4, content: '人际关系和谐。', tip: '维护关系' },
            wealth: { score: 4, content: '合作带来好运。', tip: '寻找伙伴' },
            luckyNumber: '2', luckyColor: '粉红色', luckyDirection: '北方',
            goldSentence: '好的关系是两个人一起浇灌。',
            reversedMeaning: '关系不平衡或冲突。'
        },
        {
            id: 'cups-3', name: '圣杯三 Three of Cups', emoji: '🎉',
            suit: '圣杯', suitElement: '水',
            keywords: ['友谊', '社区', '庆祝', '欢乐', '社群'],
            summary: '与朋友在一起的欢乐时光',
            coreEnergy: '社群与友谊的欢乐',
            guidance: `🎉 【关于圣杯三】

三个女人手持圣杯，欢快地舞蹈。

【今日课题】
今天约一个朋友，不需要有任何计划，就是见面聊聊。`,
            love: { score: 5, content: '朋友聚会或社交活动。', tip: '享受友谊' },
            career: { score: 4, content: '团队庆祝。', tip: '参与社群' },
            health: { score: 4, content: '社交带来快乐。', tip: '和朋友一起活动' },
            wealth: { score: 4, content: '社交带来机会。', tip: '扩展圈子' },
            luckyNumber: '3', luckyColor: '绿色', luckyDirection: '东方',
            goldSentence: '有些时光存在的意义，就是存在。',
            reversedMeaning: '社交过度或关系冲突。'
        },
        {
            id: 'cups-4', name: '圣杯四 Four of Cups', emoji: '😌',
            suit: '圣杯', suitElement: '水',
            keywords: ['忧郁', '不满', '内省', '冷漠', '沉思'],
            summary: '对眼前的一切感到无聊，需要换个角度',
            coreEnergy: '在平淡中发现新的意义',
            guidance: `😌 【关于圣杯四】

一个人坐在树下，面前摆着三杯水，他却没有看见。

【今日课题】
今天注意一下你身边习以为常的东西——它们都在这里。`,
            love: { score: 2, content: '对感情感到厌倦。', tip: '发现新的美好' },
            career: { score: 2, content: '工作动力不足。', tip: '寻找新意义' },
            health: { score: 3, content: '有些倦怠。', tip: '休息一下' },
            wealth: { score: 2, content: '对财务状况不满。', tip: '改变视角' },
            luckyNumber: '4', luckyColor: '蓝色', luckyDirection: '西方',
            goldSentence: '幸福不是没有痛苦，是知道欣赏平静。',
            reversedMeaning: '持续的忧郁或自怜。'
        },
        {
            id: 'cups-5', name: '圣杯五 Five of Cups', emoji: '🌧️',
            suit: '圣杯', suitElement: '水',
            keywords: ['失落', '悲伤', '后悔', '失去', '接受'],
            summary: '打翻的杯子流走了，但还有更多在身后',
            coreEnergy: '在失去中寻找新的希望',
            guidance: `🌧️ 【关于圣杯五】

一个人跪在地上，看着打翻的杯子。但在他身后，还有两个杯子稳稳地站着。

【今日课题】
今天如果想起一些后悔的事，告诉自己：过去的已经过去了。`,
            love: { score: 2, content: '回忆过去的失落。', tip: '放下过去' },
            career: { score: 2, content: '项目失败或挫折。', tip: '从失败中学习' },
            health: { score: 3, content: '情绪低落。', tip: '寻求支持' },
            wealth: { score: 2, content: '财务损失。', tip: '止损' },
            luckyNumber: '5', luckyColor: '深蓝色', luckyDirection: '西方',
            goldSentence: '后悔是镜子，不是牢笼。',
            reversedMeaning: '沉溺于过去或持续悲伤。'
        },
        {
            id: 'cups-6', name: '圣杯六 Six of Cups', emoji: '🌸',
            suit: '圣杯', suitElement: '水',
            keywords: ['怀旧', '童年', '回忆', '纯真', '重来'],
            summary: '回到美好的过去，从回忆中汲取温暖',
            coreEnergy: '在回忆中找到治愈',
            guidance: `🌸 【关于圣杯六】

两个孩子拿着花朵，把花递向对方。这是童年记忆中的场景。

【今日课题】
今天可以翻翻老照片、听听老歌，让回忆给你温暖。`,
            love: { score: 4, content: '怀旧带来美好的感情。', tip: '重温美好回忆' },
            career: { score: 3, content: '回顾过去的成功经验。', tip: '借鉴过去' },
            health: { score: 3, content: '童年回忆带来疗愈。', tip: '联系老朋友' },
            wealth: { score: 3, content: '老客户或回头客。', tip: '维护旧关系' },
            luckyNumber: '6', luckyColor: '浅蓝色', luckyDirection: '东方',
            goldSentence: '回忆是宝藏，但生活在此刻。',
            reversedMeaning: '沉溺过去或幼稚。'
        },
        {
            id: 'cups-7', name: '圣杯七 Seven of Cups', emoji: '🎭',
            suit: '圣杯', suitElement: '水',
            keywords: ['幻想', '选择', '诱惑', '混乱', '愿景'],
            summary: '太多美好的幻想，你需要选择一个',
            coreEnergy: '在诱惑中保持清醒',
            guidance: `🎭 【关于圣杯七】

一个人站在七杯酒前，每一杯都映出不同的幻象。

【今日课题】
写下你最近在纠结的事。然后问自己：抛开幻想，真实的是什么？`,
            love: { score: 3, content: '太多选择或幻想。', tip: '看清现实' },
            career: { score: 3, content: '方向太多，难以选择。', tip: '专注' },
            health: { score: 3, content: '想太多。', tip: '行动' },
            wealth: { score: 3, content: '太多诱人的机会。', tip: '辨别真伪' },
            luckyNumber: '7', luckyColor: '蓝色', luckyDirection: '南方',
            goldSentence: '选择是放弃的艺术。',
            reversedMeaning: '被幻想迷惑或逃避选择。'
        },
        {
            id: 'cups-8', name: '圣杯八 Eight of Cups', emoji: '🚶',
            suit: '圣杯', suitElement: '水',
            keywords: ['离开', '放弃', '寻找更深', '旅程', '决定'],
            summary: '放下现有的，转身走向更深处',
            coreEnergy: '有意义的离开',
            guidance: `🚶 【关于圣杯八】

一个人拄着杖，背对着他的八个杯子，沿着月光下的路离开。

【今日课题】
今天如果对现状不满意，问自己：是真的不满意，还是不知道自己要什么？`,
            love: { score: 2, content: '离开一段感情或状态。', tip: '寻找更深的意义' },
            career: { score: 3, content: '职业转换或离职。', tip: '寻找新的方向' },
            health: { score: 3, content: '改变生活方式。', tip: '寻找更深层的满足' },
            wealth: { score: 2, content: '放弃旧的投资。', tip: '重新开始' },
            luckyNumber: '8', luckyColor: '靛蓝色', luckyDirection: '西方',
            goldSentence: '离开是为了找到真正属于自己的。',
            reversedMeaning: '害怕离开或错误的离开。'
        },
        {
            id: 'cups-9', name: '圣杯九 Nine of Cups', emoji: '🌙',
            suit: '圣杯', suitElement: '水',
            keywords: ['满足', '愿望成真', '快乐', '温暖', '舒适'],
            summary: '愿望清单正在一项项实现',
            coreEnergy: '愿望满足的幸福',
            guidance: `🌙 【关于圣杯九】

一个人坐在那里，身后九杯酒排成半圆形，脸上带着满足的微笑。

【今日课题】
今天找一点时间，静下来感受一下：我现在拥有什么？`,
            love: { score: 5, content: '感情上的满足。', tip: '感恩' },
            career: { score: 5, content: '工作上的成就。', tip: '庆祝' },
            health: { score: 4, content: '身心满足。', tip: '保持' },
            wealth: { score: 5, content: '愿望实现！', tip: '享受成果' },
            luckyNumber: '9', luckyColor: '蓝色', luckyDirection: '东方',
            goldSentence: '感恩是丰盛的入口。',
            reversedMeaning: '不满足或虚假的安全感。'
        },
        {
            id: 'cups-10', name: '圣杯十 Ten of Cups', emoji: '🏡',
            suit: '圣杯', suitElement: '水',
            keywords: ['家庭', '和谐', '幸福', '承诺', '社区'],
            summary: '家庭和社区带来的深層满足',
            coreEnergy: '归属感与和谐',
            guidance: `🏡 【关于圣杯十】

一对夫妻相互拥抱，两个孩子在房子前嬉戏。十杯水在空中排成弧线。

【今日课题】
今天给家人打个电话，或者回家看看。`,
            love: { score: 5, content: '家庭幸福或婚礼！', tip: '珍惜家人' },
            career: { score: 4, content: '事业与家庭平衡。', tip: '家庭支持事业' },
            health: { score: 4, content: '家庭带来健康。', tip: '享受家庭时光' },
            wealth: { score: 4, content: '家庭财务稳定。', tip: '共同理财' },
            luckyNumber: '10', luckyColor: '绿色', luckyDirection: '东方',
            goldSentence: '家是起点，也是终点。',
            reversedMeaning: '家庭冲突或不和谐。'
        },
        {
            id: 'cups-page', name: '圣杯侍从 Page of Cups', emoji: '🧒',
            suit: '圣杯', suitElement: '水',
            keywords: ['创意', '直觉', '敏感', '好奇心', '情感'],
            summary: '让直觉带你去看见看不见的世界',
            coreEnergy: '创造性与直觉的萌芽',
            guidance: `🧒 【关于圣杯侍从】

一个孩子在海边，手里拿着圣杯，杯中游出一条小鱼。

【今日课题】
今天如果有一个"荒谬"的想法，不要评价它。写下来。`,
            love: { score: 4, content: '浪漫的直觉。', tip: '相信直觉' },
            career: { score: 4, content: '创意涌现。', tip: '表达创意' },
            health: { score: 3, content: '情感敏感。', tip: '照顾情绪' },
            wealth: { score: 3, content: '财务直觉。', tip: '相信第六感' },
            luckyNumber: '11', luckyColor: '蓝绿色', luckyDirection: '西方',
            goldSentence: '直觉是你内心的智慧。',
            reversedMeaning: '情感幼稚或压抑情绪。'
        },
        {
            id: 'cups-knight', name: '圣杯骑士 Knight of Cups', emoji: '🐴💙',
            suit: '圣杯', suitElement: '水',
            keywords: ['浪漫', '想象力', '魅力', '情感', '诗意'],
            summary: '带着浪漫和想象力向你走来',
            coreEnergy: '充满诗意的情感追求',
            guidance: `🐴💙 【关于圣杯骑士】

骑士骑着白马，手中托着圣杯，缓缓前行。

【今日课题】
今天做一件事，不要想"有没有用"，只问"它美不美"。`,
            love: { score: 5, content: '浪漫的相遇或约会。', tip: '接受浪漫' },
            career: { score: 3, content: '想象力和创意。', tip: '追求梦想' },
            health: { score: 3, content: '情感丰富。', tip: '表达情感' },
            wealth: { score: 3, content: '财务上的浪漫。', tip: '享受当下' },
            luckyNumber: '12', luckyColor: '蓝色', luckyDirection: '西方',
            goldSentence: '浪漫不是浪费，是让生活值得过。',
            reversedMeaning: '不切实际或情感逃避。'
        },
        {
            id: 'cups-queen', name: '圣杯皇后 Queen of Cups', emoji: '👸',
            suit: '圣杯', suitElement: '水',
            keywords: ['温暖', '直觉', '敏感', '关怀', '慈悲'],
            summary: '用温暖和直觉来照顾这个世界',
            coreEnergy: '充满爱的女性能量',
            guidance: `👸 【关于圣杯皇后】

皇后坐在海边的贝壳上，手中托着圣杯，目光温柔而深邃。

【今日课题】
今天对自己温柔一点。你已经尽力了。`,
            love: { score: 5, content: '充满爱和被爱。', tip: '给予和接受爱' },
            career: { score: 4, content: '关怀的领导。', tip: '以温柔领导' },
            health: { score: 4, content: '情感疗愈。', tip: '自我照顾' },
            wealth: { score: 3, content: '内心的富足。', tip: '精神优先' },
            luckyNumber: '13', luckyColor: '蓝绿色', luckyDirection: '西方',
            goldSentence: '温柔不是软弱，是最强大的力量。',
            reversedMeaning: '过度情绪化或自我牺牲。'
        },
        {
            id: 'cups-king', name: '圣杯国王 King of Cups', emoji: '🤴',
            suit: '圣杯', suitElement: '水',
            keywords: ['平衡', '控制', '温和', '宽容', '同理心'],
            summary: '用智慧和温和来领导，从不让情绪掌控',
            coreEnergy: '成熟而平衡的情感智慧',
            guidance: `🤴 【关于圣杯国王】

国王坐在海上的王座，手中掌握着圣杯，目光平和而深邃。

【今日课题】
今天如果遇到情绪波动，不要压制它。承认它，感受它。`,
            love: { score: 5, content: '成熟的爱。', tip: '平衡感情' },
            career: { score: 4, content: '情绪智商高。', tip: '领导有方' },
            health: { score: 4, content: '情绪稳定。', tip: '保持平衡' },
            wealth: { score: 4, content: '财务稳定。', tip: '稳健管理' },
            luckyNumber: '14', luckyColor: '深蓝色', luckyDirection: '西方',
            goldSentence: '能够感受情绪的人，才能真正掌控情绪。',
            reversedMeaning: '情绪失控或冷漠。'
        }
    ],

    // 宝剑牌组 (Swords) - 风元素 - 智慧、思想、沟通、冲突
    swords: [
        {
            id: 'swords-ace', name: '宝剑王牌 Ace of Swords', emoji: '⚡',
            suit: '宝剑', suitElement: '风',
            keywords: ['突破', '清晰', '真相', '新的思维', '決断'],
            summary: '真相的剑刺穿迷雾，清晰到来',
            coreEnergy: '穿透迷雾的智慧之剑',
            guidance: `⚡ 【关于宝剑Ace】

一把剑从云中刺下，剑尖穿透皇冠和玫瑰。

【今日课题】
今天有没有一件事，你一直在骗自己？给自己一个诚实的答案。`,
            love: { score: 3, content: '真相大白。', tip: '诚实面对' },
            career: { score: 4, content: '突破思维。', tip: '新的想法' },
            health: { score: 3, content: '清晰的思维。', tip: '决定健康选择' },
            wealth: { score: 4, content: '财务决策清晰。', tip: '理性分析' },
            luckyNumber: '1', luckyColor: '银色', luckyDirection: '东方',
            goldSentence: '真相可能痛，但比谎言自由。',
            reversedMeaning: '混乱或错误判断。'
        },
        {
            id: 'swords-2', name: '宝剑二 Two of Swords', emoji: '⚖️',
            suit: '宝剑', suitElement: '风',
            keywords: ['平衡', '抉择', '犹豫不决', '暂时停滯', '中立'],
            summary: '站在两个选择之间，需要更多时间',
            coreEnergy: '在冲突中寻找平衡',
            guidance: `⚖️ 【关于宝剑二】

一个女人坐在石椅上，双手各持一剑。她蒙着眼睛。

【今日课题】
如果你正在纠结一件事，问自己：是真的需要现在决定吗？`,
            love: { score: 3, content: '难以选择。', tip: '等待时机' },
            career: { score: 3, content: '暂停决定。', tip: '收集更多信息' },
            health: { score: 3, content: '保持平衡。', tip: '不偏不倚' },
            wealth: { score: 3, content: '观望。', tip: '暂不行动' },
            luckyNumber: '2', luckyColor: '灰色', luckyDirection: '西方',
            goldSentence: '等待不是逃避，是尊重时机。',
            reversedMeaning: '无法决定或长期犹豫。'
        },
        {
            id: 'swords-3', name: '宝剑三 Three of Swords', emoji: '💔',
            suit: '宝剑', suitElement: '风',
            keywords: ['心痛', '悲伤', '失落', '痛苦', '接受'],
            summary: '心被剑刺穿，但伤口会愈合',
            coreEnergy: '在痛苦中允许自己悲伤',
            guidance: `💔 【关于宝剑三】

三把剑刺入一颗心。

【今日课题】
今天如果感到伤心，给自己一个空间。悲伤不需要理由。`,
            love: { score: 2, content: '心痛或失望。', tip: '允许自己悲伤' },
            career: { score: 2, content: '困难的决定。', tip: '寻求支持' },
            health: { score: 2, content: '心痛影响身体。', tip: '照顾自己' },
            wealth: { score: 2, content: '财务心痛。', tip: '面对现实' },
            luckyNumber: '3', luckyColor: '深灰色', luckyDirection: '西方',
            goldSentence: '允许自己悲伤，才是真正的疗愈开始。',
            reversedMeaning: '拒绝悲伤或持续痛苦。'
        },
        {
            id: 'swords-4', name: '宝剑四 Four of Swords', emoji: '🛡️',
            suit: '宝剑', suitElement: '风',
            keywords: ['休息', '恢复', '内省', '独处', '暂停'],
            summary: '暂时的退出，是为了更好地回来',
            coreEnergy: '在休息中重新整合',
            guidance: `🛡️ 【关于宝剑四】

一个人躺在教堂的石棺上，双手叠放，安静地休息。

【今日课题】
今天如果累了，就休息。不要说"再等一下"。`,
            love: { score: 3, content: '需要独处时间。', tip: '休息' },
            career: { score: 2, content: '需要休息。', tip: '暂停' },
            health: { score: 4, content: '身体需要恢复。', tip: '充分休息' },
            wealth: { score: 3, content: '财务暂停。', tip: '观望' },
            luckyNumber: '4', luckyColor: '蓝灰色', luckyDirection: '北方',
            goldSentence: '休息不是偷懒，暂停不是放弃。',
            reversedMeaning: '休息过度或逃避。'
        },
        {
            id: 'swords-5', name: '宝剑五 Five of Swords', emoji: '🏃',
            suit: '宝剑', suitElement: '风',
            keywords: ['失败', '损失', '冲突', '背叛', '争炒'],
            summary: '输了战斗，但赢得了教训',
            coreEnergy: '在失败中寻找教训',
            guidance: `🏃 【关于宝剑五】

胜利者拿着剑离开，留下一地残局。

【今日课题】
今天如果遇到失败，问自己：我学到了什么？`,
            love: { score: 2, content: '冲突或争吵。', tip: '和解' },
            career: { score: 2, content: '失败或挫折。', tip: '学习' },
            health: { score: 2, content: '争强失败。', tip: '退让' },
            wealth: { score: 2, content: '财务损失。', tip: '止损' },
            luckyNumber: '5', luckyColor: '灰色', luckyDirection: '西方',
            goldSentence: '输赢不重要，成长才重要。',
            reversedMeaning: '赢得冲突但失去更多。'
        },
        {
            id: 'swords-6', name: '宝剑六 Six of Swords', emoji: '🚣',
            suit: '宝剑', suitElement: '风',
            keywords: ['过渡', '移动', '疗愈', '从痛苦中离开', '向前走'],
            summary: '正在离开痛苦的水域，驶向平静的水域',
            coreEnergy: '从苦难中驶向疗愈',
            guidance: `🚣 【关于宝剑六】

一艘小船载着一个人驶向远方。水面从混乱变得平静。

【今日课题】
今天想一件你正在"离开"的事。允许自己为过去画一个句号。`,
            love: { score: 3, content: '从痛苦中恢复。', tip: '向前走' },
            career: { score: 3, content: '过渡时期。', tip: '适应新环境' },
            health: { score: 3, content: '康复中。', tip: '继续疗愈' },
            wealth: { score: 3, content: '财务过渡。', tip: '重新规划' },
            luckyNumber: '6', luckyColor: '浅蓝色', luckyDirection: '西方',
            goldSentence: '离开不是为了逃避，是为了疗愈。',
            reversedMeaning: '抗拒改变或无法前进。'
        },
        {
            id: 'swords-7', name: '宝剑七 Seven of Swords', emoji: '🎭',
            suit: '宝剑', suitElement: '风',
            keywords: ['策略', '计划', '隐秘', '单独行动', '欺骗'],
            summary: '用智慧而不是力量来赢得胜利',
            coreEnergy: '在困境中寻找出路',
            guidance: `🎭 【关于宝剑七】

一个人偷偷地从军营拿走五把剑，留下两把。

【今日课题】
今天如果遇到挑战，问自己：除了明显的方法，还有什么方法？`,
            love: { score: 2, content: '小心欺骗。', tip: '诚实' },
            career: { score: 4, content: '策略性思考。', tip: '智取' },
            health: { score: 3, content: '需要策略。', tip: '谨慎行动' },
            wealth: { score: 4, content: '财务策略。', tip: '精明投资' },
            luckyNumber: '7', luckyColor: '银色', luckyDirection: '西方',
            goldSentence: '智慧是知道什么时候该进，什么时候该退。',
            reversedMeaning: '欺骗或被抓。'
        },
        {
            id: 'swords-8', name: '宝剑八 Eight of Swords', emoji: '🔒',
            suit: '宝剑', suitElement: '风',
            keywords: ['被困', '限制', '无助', '困境', '自我设限'],
            summary: '被束缚的感觉，但绑住你的其实是你自己',
            coreEnergy: '打破内心的束缚',
            guidance: `🔒 【关于宝剑八】

一个女人被绑在木桩上，周围插着八把剑。她蒙着眼睛，但绑她的绳子其实是松的。

【今日课题】
今天如果感到被困，问自己：是什么困住了我？是真的不能，还是我以为不能？`,
            love: { score: 2, content: '感到被困在感情中。', tip: '你有选择' },
            career: { score: 2, content: '工作限制。', tip: '打破限制' },
            health: { score: 2, content: '被困住的感觉。', tip: '寻求帮助' },
            wealth: { score: 2, content: '财务受限。', tip: '寻找新方案' },
            luckyNumber: '8', luckyColor: '深灰色', luckyDirection: '西方',
            goldSentence: '你比自己以为的更自由。',
            reversedMeaning: '自我囚禁或放弃挣扎。'
        },
        {
            id: 'swords-9', name: '宝剑九 Nine of Swords', emoji: '😰',
            suit: '宝剑', suitElement: '风',
            keywords: ['焦虑', '恐惧', '担忧', '失眠', '过度思考'],
            summary: '深夜的焦虑，太阳升起就会散去',
            coreEnergy: '在焦虑的夜晚相信黎明会来',
            guidance: `😰 【关于宝剑九】

一个女人坐在床上，双手捂脸，身后九把剑插在墙上。

【今日课题】
今天如果很焦虑，告诉自己：这会过去的。`,
            love: { score: 2, content: '焦虑或恐惧。', tip: '直面恐惧' },
            career: { score: 3, content: '担忧工作。', tip: '放松' },
            health: { score: 2, content: '焦虑影响睡眠。', tip: '好好休息' },
            wealth: { score: 3, content: '财务焦虑。', tip: '做预算' },
            luckyNumber: '9', luckyColor: '灰色', luckyDirection: '南方',
            goldSentence: '焦虑是对还没有发生的事的想象。',
            reversedMeaning: '严重的焦虑或恐慌。'
        },
        {
            id: 'swords-10', name: '宝剑十 Ten of Swords', emoji: '🌅',
            suit: '宝剑', suitElement: '风',
            keywords: ['崩溃', '结束', '彻底改变', '死亡与重生', '最低点'],
            summary: '跌到谷底，但最低点也是新的起点',
            coreEnergy: '在崩溃中发现新生',
            guidance: `🌅 【关于宝剑十】

一个人趴在地下，十把剑插在他身上。黎明在远方。

【今日课题】
今天如果感到已经到了极限，问自己：最坏的情况是什么？然后告诉自己：我能承受。`,
            love: { score: 2, content: '感情的最低点。', tip: '触底反弹' },
            career: { score: 2, content: '事业崩溃。', tip: '重新开始' },
            health: { score: 2, content: '健康最差。', tip: '开始康复' },
            wealth: { score: 2, content: '财务最低点。', tip: '重新起步' },
            luckyNumber: '10', luckyColor: '黑色', luckyDirection: '东方',
            goldSentence: '最低点是地板，不是天花板。',
            reversedMeaning: '拒绝改变或持续的痛苦。'
        },
        {
            id: 'swords-page', name: '宝剑侍从 Page of Swords', emoji: '🧒⚔️',
            suit: '宝剑', suitElement: '风',
            keywords: ['好奇心', '求真', '敏捷思维', '挑战', '学习'],
            summary: '带着好奇心追求真相的年轻人',
            coreEnergy: '渴望知识的年轻求真者',
            guidance: `🧒⚔️ 【关于宝剑侍从】

一个年轻人手持剑，站在山崖上，望着远方的云层。

【今日课题】
今天有没有一个你一直不敢问的问题？问吧。`,
            love: { score: 3, content: '好奇地探索感情。', tip: '问问题' },
            career: { score: 4, content: '学习新技能。', tip: '好奇心' },
            health: { score: 3, content: '保持敏捷。', tip: '多思考' },
            wealth: { score: 3, content: '新的财务想法。', tip: '学习理财' },
            luckyNumber: '11', luckyColor: '黄色', luckyDirection: '东方',
            goldSentence: '问题的答案比问题本身更重要。',
            reversedMeaning: '肤浅或回避真相。'
        },
        {
            id: 'swords-knight', name: '宝剑骑士 Knight of Swords', emoji: '🏇',
            suit: '宝剑', suitElement: '风',
            keywords: ['行动', '决心', '意志', '冲刺', '野心'],
            summary: '带着清晰的意图和速度向前冲',
            coreEnergy: '全速前进的决心',
            guidance: `🏇 【关于宝剑骑士】

骑士骑着白马，手持剑，目光如炬，向着目标全力冲刺。

【今日课题】
今天如果需要快速行动，问自己：我是深思熟虑后的快速，还是冲动的快速？`,
            love: { score: 3, content: '快速追求。', tip: '不要冲动' },
            career: { score: 4, content: '快速行动。', tip: '但要专注' },
            health: { score: 3, content: '快速行动。', tip: '注意安全' },
            wealth: { score: 4, content: '快速决策。', tip: '不要犹豫' },
            luckyNumber: '12', luckyColor: '银色', luckyDirection: '南方',
            goldSentence: '速度是工具，不是目的。',
            reversedMeaning: '冲动或鲁莽。'
        },
        {
            id: 'swords-queen', name: '宝剑皇后 Queen of Swords', emoji: '👸⚔️',
            suit: '宝剑', suitElement: '风',
            keywords: ['智慧', '清晰', '同理心', '独立', '界限'],
            summary: '用智慧和同理心来判断，不带偏见',
            coreEnergy: '成熟而独立的智慧',
            guidance: `👸⚔️ 【关于宝剑皇后】

皇后坐在云端宝座，手中持剑，目光温柔而清明。

【今日课题】
今天做一个决定时，问自己：我的决定是基于事实，还是基于情绪？`,
            love: { score: 4, content: '清晰的感情判断。', tip: '同理心' },
            career: { score: 5, content: '智慧领导。', tip: '公平判断' },
            health: { score: 4, content: '清晰的健康判断。', tip: '独立思考' },
            wealth: { score: 4, content: '精明理财。', tip: '设立界限' },
            luckyNumber: '13', luckyColor: '蓝灰色', luckyDirection: '西方',
            goldSentence: '最好的决定是心与脑的共识。',
            reversedMeaning: '冷酷或偏见。'
        },
        {
            id: 'swords-king', name: '宝剑国王 King of Swords', emoji: '🤴⚔️',
            suit: '宝剑', suitElement: '风',
            keywords: ['权威', '真相', '清晰思考', '道德', '决策'],
            summary: '用最高的智慧和道德来统治',
            coreEnergy: '正直而权威的智慧',
            guidance: `🤴⚔️ 【关于宝剑国王】

国王坐在宝座上，手持宝剑，目光如鹰。

【今日课题】
今天如果有人说了一些你不爱听的话，谢谢他。`,
            love: { score: 4, content: '公正的判断。', tip: '真相优先' },
            career: { score: 5, content: '领导力强。', tip: '做决定' },
            health: { score: 4, content: '清晰的思维。', tip: '坚持原则' },
            wealth: { score: 5, content: '财务决策英明。', tip: '权威决策' },
            luckyNumber: '14', luckyColor: '银色', luckyDirection: '西方',
            goldSentence: '真相让你自由，但首先会让你不舒服。',
            reversedMeaning: '滥用权威或独裁。'
        }
    ],

    // 五芒星牌组 (Pentacles) - 土元素 - 物质、财富、健康、工作
    pentacles: [
        {
            id: 'pentacles-ace', name: '五芒星王牌 Ace of Pentacles', emoji: '🌱',
            suit: '五芒星', suitElement: '土',
            keywords: ['新的机会', '财务', '物质', '实际', '开始'],
            summary: '一个新的物质机会正在向你招手',
            coreEnergy: '落地的创造力开始显化',
            guidance: `🌱 【关于五芒星Ace】

一只手从云中伸出，托着一颗五芒星。

【今日课题】
今天有没有一个机会，你只是看看，没有伸手？告诉自己：可以试试。`,
            love: { score: 3, content: '实际的感情机会。', tip: '把握机会' },
            career: { score: 5, content: '新的工作机会！', tip: '伸手' },
            health: { score: 4, content: '新的健康计划。', tip: '开始养生' },
            wealth: { score: 5, content: '新的财务机会！', tip: '抓住' },
            luckyNumber: '1', luckyColor: '绿色', luckyDirection: '东方',
            goldSentence: '机会不等人，但也不强求。',
            reversedMeaning: '错失机会或缺乏行动。'
        },
        {
            id: 'pentacles-2', name: '五芒星二 Two of Pentacles', emoji: '🎭',
            suit: '五芒星', suitElement: '土',
            keywords: ['平衡', '适应', '多任务', '优先排序', '弹性'],
            summary: '在多项事务中找到平衡',
            coreEnergy: '在变化中保持平衡',
            guidance: `🎭 【关于五芒星二】

一个人在玩杂耍，两颗五芒星在空中旋转。他脚下是波浪，但他在保持平衡。

【今日课题】
今天列一个清单，然后问自己：哪些是真正重要的，哪些只是紧急的？`,
            love: { score: 3, content: '平衡感情与生活。', tip: '优先级' },
            career: { score: 4, content: '多任务处理。', tip: '找到节奏' },
            health: { score: 3, content: '工作生活平衡。', tip: '不要过度' },
            wealth: { score: 4, content: '财务平衡。', tip: '合理分配' },
            luckyNumber: '2', luckyColor: '棕色', luckyDirection: '东方',
            goldSentence: '忙不等于有效率。',
            reversedMeaning: '失衡或过度忙碌。'
        },
        {
            id: 'pentacles-3', name: '五芒星三 Three of Pentacles', emoji: '👷',
            suit: '五芒星', suitElement: '土',
            keywords: ['团队合作', '学习', '技能', '合作', '建筑'],
            summary: '团队合作让梦想变为现实',
            coreEnergy: '协作中的专业成长',
            guidance: `👷 【关于五芒星三】

一个人在石匠铺里工作，另外两个人在看着他。

【今日课题】
今天如果在一个团队项目中，问问自己：我的独特贡献是什么？`,
            love: { score: 3, content: '团队活动。', tip: '合作' },
            career: { score: 5, content: '团队合作成功！', tip: '发挥专长' },
            health: { score: 3, content: '团队运动。', tip: '协作' },
            wealth: { score: 4, content: '团队项目。', tip: '学习技能' },
            luckyNumber: '3', luckyColor: '棕色', luckyDirection: '北方',
            goldSentence: '合作是让对方的优点加上你的优点。',
            reversedMeaning: '缺乏团队精神或不专业。'
        },
        {
            id: 'pentacles-4', name: '五芒星四 Four of Pentacles', emoji: '🛡️',
            suit: '五芒星', suitElement: '土',
            keywords: ['安全', '占有欲', '守财', '稳定', '控制'],
            summary: '紧紧抓住拥有的，但要注意方式',
            coreEnergy: '在安全感中注意界限',
            guidance: `🛡️ 【关于五芒星四】

一个人蹲在地上，双手紧紧抱住五芒星。

【今日课题】
今天在钱的事情上，问问自己：我是在投资未来，还是在封死自己？`,
            love: { score: 3, content: '占有欲或安全感。', tip: '学会给予' },
            career: { score: 3, content: '稳定性强。', tip: '不要太保守' },
            health: { score: 4, content: '安全感。', tip: '维持现状' },
            wealth: { score: 4, content: '财务安全。', tip: '但不要守财' },
            luckyNumber: '4', luckyColor: '绿色', luckyDirection: '西方',
            goldSentence: '钱是工具，不是主人。',
            reversedMeaning: '贪婪或过度控制。'
        },
        {
            id: 'pentacles-5', name: '五芒星五 Five of Pentacles', emoji: '🏠',
            suit: '五芒星', suitElement: '土',
            keywords: ['困难', '财务问题', '孤独', '寻找帮助', '韧性'],
            summary: '困难时刻，但光就在前方',
            coreEnergy: '在困境中寻找希望',
            guidance: `🏠 【关于五芒星五】

两个人在风雪中走过一间亮着灯的教堂。

【今日课题】
今天如果感到困难，告诉自己：这会过去的。而且，你不是一个人在经历这个。`,
            love: { score: 2, content: '经济困难影响感情。', tip: '共同克服' },
            career: { score: 2, content: '工作困难。', tip: '寻求帮助' },
            health: { score: 2, content: '健康警报。', tip: '及时就医' },
            wealth: { score: 2, content: '财务紧张。', tip: '开源节流' },
            luckyNumber: '5', luckyColor: '灰色', luckyDirection: '西方',
            goldSentence: '最黑的黑夜之后，就是黎明。',
            reversedMeaning: '持续的困难或放弃希望。'
        },
        {
            id: 'pentacles-6', name: '五芒星六 Six of Pentacles', emoji: '💰',
            suit: '五芒星', suitElement: '土',
            keywords: ['给予', '接受', '慷慨', '财务平衡', '分享'],
            summary: '金钱在流动，有人给，有人收',
            coreEnergy: '给予与接受的平衡',
            guidance: `💰 【关于五芒星六】

一个人拿着天平，正在给两个乞丐分五芒星。

【今日课题】
今天如果有人向你求助，想想你能帮什么。不是钱的问题，是"我能给予什么"的问题。`,
            love: { score: 4, content: '给予和接受爱。', tip: '平衡付出' },
            career: { score: 4, content: '分享成果。', tip: '团队分红' },
            health: { score: 4, content: '分享健康。', tip: '帮助他人' },
            wealth: { score: 4, content: '财务平衡！', tip: '分享财富' },
            luckyNumber: '6', luckyColor: '绿色', luckyDirection: '东方',
            goldSentence: '给予和接受都是一种勇气。',
            reversedMeaning: '不平衡的给予或自私。'
        },
        {
            id: 'pentacles-7', name: '五芒星七 Seven of Pentacles', emoji: '🌿',
            suit: '五芒星', suitElement: '土',
            keywords: ['耐心', '长期投资', '等待', '坚持', '养成'],
            summary: '种子已经种下，需要时间让它生长',
            coreEnergy: '耐心等待的成长',
            guidance: `🌿 【关于五芒星七】

一个人拄着杖，看着他种下的五芒星。还没有结果，但根已经在土里生长。

【今日课题】
今天为你的"等待"做一个进度检查。我已经走了多远？还要多久？`,
            love: { score: 3, content: '感情需要耐心。', tip: '等待' },
            career: { score: 3, content: '长期项目。', tip: '持续投入' },
            health: { score: 3, content: '长期养生。', tip: '坚持' },
            wealth: { score: 4, content: '投资等待回报。', tip: '耐心持有' },
            luckyNumber: '7', luckyColor: '绿色', luckyDirection: '东方',
            goldSentence: '等待不是放弃，是给种子时间发芽。',
            reversedMeaning: '不耐烦或错误的投资。'
        },
        {
            id: 'pentacles-8', name: '五芒星八 Eight of Pentacles', emoji: '🔨',
            suit: '五芒星', suitElement: '土',
            keywords: ['工匠精神', '技能', '努力工作', '专注', '精通'],
            summary: '专注于磨练技能，技艺正在提升',
            coreEnergy: '专注与精进的工匠精神',
            guidance: `🔨 【关于五芒星八】

一个人坐在工作台前，正在精心雕刻一颗五芒星。

【今日课题】
今天找一个你想要精进的技能，花时间在上面。不需要很久，哪怕30分钟。`,
            love: { score: 3, content: '打磨感情。', tip: '专注经营' },
            career: { score: 5, content: '技能提升！', tip: '深耕' },
            health: { score: 4, content: '训练。', tip: '刻意练习' },
            wealth: { score: 4, content: '专业技能。', tip: '投资自己' },
            luckyNumber: '8', luckyColor: '棕色', luckyDirection: '东方',
            goldSentence: '工匠和普通人的区别，不在天赋，在时间。',
            reversedMeaning: '浪费时间或不专注。'
        },
        {
            id: 'pentacles-9', name: '五芒星九 Nine of Pentacles', emoji: '🏰',
            suit: '五芒星', suitElement: '土',
            keywords: ['繁荣', '独立', '自我满足', '努力回报', '舒适'],
            summary: '你的努力已经开花结果，享受这份美好',
            coreEnergy: '独立自主的繁荣',
            guidance: `🏰 【关于五芒星九】

一个女人站在花园中，周围是成熟的五芒星。

【今日课题】
今天感谢一下自己：你已经很努力了，而且你值得。`,
            love: { score: 5, content: '独立而满足。', tip: '享受单身' },
            career: { score: 5, content: '成就获得！', tip: '犒劳自己' },
            health: { score: 5, content: '健康繁荣。', tip: '保持' },
            wealth: { score: 5, content: '财务自由！', tip: '享受成果' },
            luckyNumber: '9', luckyColor: '金色', luckyDirection: '东方',
            goldSentence: '自己给自己的安全感，才是真正的安全感。',
            reversedMeaning: '虚假的安全感或傲慢。'
        },
        {
            id: 'pentacles-10', name: '五芒星十 Ten of Pentacles', emoji: '👨‍👩‍👧‍👦',
            suit: '五芒星', suitElement: '土',
            keywords: ['财富', '家庭', '遗产', '传承', '长期成功'],
            summary: '家庭的繁荣和传承，财富代代相传',
            coreEnergy: '家庭与传承的繁荣',
            guidance: `👨‍👩‍👧‍👦 【关于五芒星十】

一家人其乐融融地站在庭院中，周围是丰盛的十颗五芒星。

【今日课题】
今天想想你继承了什么——不只是钱，还有习惯、态度、价值观。然后想想你想传承什么。`,
            love: { score: 5, content: '家庭幸福！', tip: '珍惜家人' },
            career: { score: 5, content: '家族企业或传承。', tip: '长远规划' },
            health: { score: 4, content: '家族健康。', tip: '传承好习惯' },
            wealth: { score: 5, content: '财富传承！', tip: '规划遗产' },
            luckyNumber: '10', luckyColor: '金色', luckyDirection: '西方',
            goldSentence: '最大的财富不是钱，是影响。',
            reversedMeaning: '家庭冲突或财务压力。'
        },
        {
            id: 'pentacles-page', name: '五芒星侍从 Page of Pentacles', emoji: '🧒🌱',
            suit: '五芒星', suitElement: '土',
            keywords: ['学习', '志向', '财务管理', '实用知识', '成长'],
            summary: '带着学习的热情，开始你的财富之路',
            coreEnergy: '渴望学习的年轻工匠',
            guidance: `🧒🌱 【关于五芒星侍从】

一个年轻人手持五芒星，低头认真学习。

【今日课题】
今天找一个你想学习的实用技能，哪怕只是一点点。`,
            love: { score: 3, content: '学习的感情观。', tip: '成长' },
            career: { score: 4, content: '职业学习。', tip: '掌握技能' },
            health: { score: 3, content: '学习健康知识。', tip: '开始养生' },
            wealth: { score: 4, content: '学习理财。', tip: '从小处开始' },
            luckyNumber: '11', luckyColor: '棕色', luckyDirection: '东方',
            goldSentence: '开始就是进步的一半。',
            reversedMeaning: '缺乏志向或懒惰。'
        },
        {
            id: 'pentacles-knight', name: '五芒星骑士 Knight of Pentacles', emoji: '🐎',
            suit: '五芒星', suitElement: '土',
            keywords: ['勤奋', '稳定', '责任', '效率', '传统'],
            summary: '一步一步，稳定地前进',
            coreEnergy: '可靠而勤奋的前行',
            guidance: `🐎 【关于五芒星骑士】

骑士骑着一匹稳固的马，手中拿着五芒星。他不急，他只是在前进。

【今日课题】
今天做一件事，不要想着走捷径。按部就班来。`,
            love: { score: 3, content: '稳定地发展。', tip: '稳步前进' },
            career: { score: 4, content: '勤奋工作。', tip: '按部就班' },
            health: { score: 3, content: '稳定训练。', tip: '保持节奏' },
            wealth: { score: 4, content: '稳健理财。', tip: '长期投资' },
            luckyNumber: '12', luckyColor: '棕色', luckyDirection: '东方',
            goldSentence: '稳定的前进，比冲刺后放弃更好。',
            reversedMeaning: '停滞或缺乏进展。'
        },
        {
            id: 'pentacles-queen', name: '五芒星皇后 Queen of Pentacles', emoji: '👸🌸',
            suit: '五芒星', suitElement: '土',
            keywords: ['富足', '照顾', '实际', '安全感', '养育'],
            summary: '用温柔和实际来照顾自己和他人',
            coreEnergy: '充满爱与富足的滋养',
            guidance: `👸🌸 【关于五芒星皇后】

皇后坐在花园中，手中托着五芒星。

【今日课题】
今天照顾一下自己。不是奖励，是应得的照顾。`,
            love: { score: 5, content: '照顾和被照顾。', tip: '爱自己' },
            career: { score: 4, content: '照顾团队。', tip: '关怀下属' },
            health: { score: 5, content: '自我照顾。', tip: '养生' },
            wealth: { score: 4, content: '财务照顾。', tip: '管理好钱' },
            luckyNumber: '13', luckyColor: '绿色', luckyDirection: '东方',
            goldSentence: '照顾好自己，才能照顾别人。',
            reversedMeaning: '过度照顾或忽视自己。'
        },
        {
            id: 'pentacles-king', name: '五芒星国王 King of Pentacles', emoji: '🤴🌳',
            suit: '五芒星', suitElement: '土',
            keywords: ['成功', '繁荣', '领导', '物质保障', '商业'],
            summary: '在物质世界中取得了成功',
            coreEnergy: '成功而慷慨的领导',
            guidance: `🤴🌳 【关于五芒星国王】

国王坐在大自然的宝座上，手持五芒星。

【今日课题】
今天在财务上做一个决定，不要只看眼前，想想长远。`,
            love: { score: 4, content: '稳定的感情。', tip: '长远考虑' },
            career: { score: 5, content: '商业成功！', tip: '扩大业务' },
            health: { score: 4, content: '健康稳定。', tip: '维持' },
            wealth: { score: 5, content: '财务成功！', tip: '投资未来' },
            luckyNumber: '14', luckyColor: '金色', luckyDirection: '西方',
            goldSentence: '真正的富有不是有多少，是需要的时候够不够。',
            reversedMeaning: '贪婪或物质主义。'
        }
    ]
};

// 获取所有78张牌
function getAllCards() {
    const major = tarotDeck.majorArcana;
    const wands = tarotDeck.wands.map(c => ({...c, suit: '权杖'}));
    const cups = tarotDeck.cups.map(c => ({...c, suit: '圣杯'}));
    const swords = tarotDeck.swords.map(c => ({...c, suit: '宝剑'}));
    const pentacles = tarotDeck.pentacles.map(c => ({...c, suit: '五芒星'}));
    
    return [...major, ...wands, ...cups, ...swords, ...pentacles];
}

// 获取随机一张牌
function getRandomCard() {
    const allCards = getAllCards();
    const index = Math.floor(Math.random() * allCards.length);
    return allCards[index];
}
