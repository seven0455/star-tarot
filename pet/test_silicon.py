import urllib.request
import json

# 硅基流动API测试
url = 'https://api.siliconflow.cn/v1/chat/completions'
data = {
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "messages": [{"role": "user", "content": "你好"}],
    "max_tokens": 50
}

req = urllib.request.Request(
    url,
    data=json.dumps(data).encode('utf-8'),
    headers={
        'Authorization': 'Bearer sk-gilimhvnuuskerfpdwfkcqvzvcuokggcyhepbocjhgimkep',
        'Content-Type': 'application/json'
    }
)

try:
    r = urllib.request.urlopen(req, timeout=10)
    resp = json.loads(r.read().decode('utf-8'))
    print('成功!')
    print(resp.get('choices', [{}])[0].get('message', {}).get('content', ''))
except Exception as e:
    print('失败:', e)
