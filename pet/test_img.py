import urllib.request
import json

url = 'https://api.siliconflow.cn/v1/images/generations'
data = {
    'model': 'FLUX-def',
    'prompt': 'mystical tarot card design, deep purple starry night background, a glowing mystical eye wearing elegant crown, gold and purple, celestial stars, moon, magical mysterious atmosphere, app icon square'
}

req = urllib.request.Request(url, data=json.dumps(data).encode(), headers={
    'Authorization': 'Bearer sk-gilimhvnuuskerfpdwfkcqvzvcuokggcyhepbocjhgimkep',
    'Content-Type': 'application/json'
})

try:
    r = urllib.request.urlopen(req, timeout=30)
    resp = json.loads(r.read())
    print('成功:', resp)
except Exception as e:
    print('失败:', e)
