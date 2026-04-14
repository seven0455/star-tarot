import urllib.request
import json

# 测试36kr API
url = 'https://36kr.com/api/newsflash?per_page=10&page=1'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://36kr.com/'
})

try:
    r = urllib.request.urlopen(req, timeout=10)
    raw = r.read()
    print('Raw bytes:', len(raw))
    
    # 尝试utf-8
    try:
        text = raw.decode('utf-8')
    except:
        text = raw.decode('gbk', errors='ignore')
    
    print('First 500 chars:', text[:500])
    
    data = json.loads(text)
    items = data.get('data', {}).get('items', [])
    print(f'\nFound {len(items)} items')
    for item in items[:3]:
        print(f"- {item.get('title')}")
        
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
