import urllib.request
import json

url = 'https://36kr.com/api/newsflash?per_page=8&page=1'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://36kr.com/',
})
r = urllib.request.urlopen(req, timeout=10)
raw = r.read()

print('Raw bytes:', len(raw))
print('First 100 bytes hex:', raw[:100].hex())

# 尝试不同编码
for enc in ['utf-8', 'gbk', 'gb2312', 'gb18030']:
    try:
        text = raw.decode(enc)
        print('Decoded with', enc, ':', text[:100])
        break
    except Exception as e:
        print('Failed', enc, ':', e)
