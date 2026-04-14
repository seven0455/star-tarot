import urllib.request
import json
import sys

# 设置输出编码
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2517&k=&num=10&page=1&r=0.5'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Referer': 'https://tech.sina.com.cn/'
})

try:
    r = urllib.request.urlopen(req, timeout=10)
    text = r.read().decode('utf-8', errors='ignore')
    data = json.loads(text)
    
    items = data.get('result', {}).get('data', [])
    print('Number of items:', len(items))
    
    # 保存到文件
    with open('C:/.openclaw/workspace/pet/news_test.txt', 'w', encoding='utf-8') as f:
        for i, item in enumerate(items[:10]):
            f.write(f"{i+1}. {item.get('title')}\n")
    print('Saved to news_test.txt')
    
except Exception as e:
    print('Error:', e)
