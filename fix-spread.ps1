$content = Get-Content "C:\.openclaw\workspace\pet\star-tarot\index.html" -Raw
$oldFunc = @'
        function requestSpreadAI() {
            // 获取三张牌的信息发送给AI
            const cardsInfo = spreadCards.map((card, i) => {
                const pos = ['过去', '现在', '未来'][i];
                return `${pos}: ${card.name} (${card.emoji})`;
            }).join(' | ');
            
            alert('正在调用AI解读...
三牌阵: ' + cardsInfo);
            // 这里可以调用server.py的/chat接口
        }
'@

$newFunc = @'
        function requestSpreadAI() {
            const loadingDiv = document.createElement('div');
            loadingDiv.style.cssText = 'text-align:center; padding:20px; color:rgba(255,255,255,0.7);';
            loadingDiv.innerHTML = '🤖 小七正在思考中...';
            document.getElementById('spreadResult').appendChild(loadingDiv);
            
            // 构建三牌阵信息
            const cardsInfo = spreadCards.map((card, i) => {
                const pos = ['过去', '现在', '未来'][i];
                return `${pos}【${card.name}】\n关键词: ${card.keywords ? card.keywords.join(', ') : '无'}\n解读: ${card.summary || card.meaning || ''}`;
            }).join('\n\n');
            
            fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: `message=请深度解读三牌阵：\n\n${cardsInfo}\n\n请结合三张牌的能量关系给出综合分析，包括：1.三牌之间的联系 2.具体领域的解读 3.行动建议`
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById('spreadResult').innerHTML = `
                    <div style="padding:20px; background:rgba(67,233,123,0.1); border-radius:16px; margin:20px 0;">
                        <div style="font-size:14px; font-weight:600; color:#43e97b; margin-bottom:15px;">✨ AI综合解读 ✨</div>
                        <div style="font-size:13px; line-height:2; color:rgba(255,255,255,0.85); white-space:pre-wrap;">${data.reply || '小七暂时无法回应，请稍后再试。'}</div>
                    </div>
                    <div style="text-align:center;">
                        <button onclick="showSpreadResult()" style="padding:10px 20px; background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); border-radius:20px; color:rgba(255,255,255,0.7); cursor:pointer;">返回牌阵</button>
                    </div>
                `;
            })
            .catch(err => {
                loadingDiv.innerHTML = '❌ 小七暂时无法回应，请稍后再试。';
            });
        }
'@

$content = $content.Replace($oldFunc, $newFunc)
$content | Out-File -FilePath "C:\.openclaw\workspace\pet\star-tarot\index.html" -Encoding UTF8 -NoNewline
Write-Host "Done"