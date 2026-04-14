#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小七对话服务器
接收网页消息，调用MiniMax API，返回AI回复
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import json
import urllib.parse

API_KEY = "sk-cp-h5YMa2sWLEzaYwsY27tNgND92OTax39v1OKfdbglV_IKuQOlaFx6NuB3V2ZvL2lMLbbonNmK82MItPm6vFn6MR4_IJvy_pKmZv_nxADiYwrQmif8CAZIcmQ"
API_URL = "https://api.minimaxi.com/v1/text/chatcompletion_v2"

def chat_with_minimax(message):
    """调用MiniMax API"""
    data = {
        "model": "MiniMax-M2.7",
        "messages": [{"role": "user", "content": message}],
        "max_tokens": 200,
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
            return resp['choices'][0]['message']['content']
    except Exception as e:
        return f"抱歉，出错了: {e}"
    
    return "小七没收到回复呢..."

class ChatHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            
            message = params.get('message', [''])[0]
            
            if message:
                # 调用AI
                reply = chat_with_minimax(message)
            else:
                reply = "小七没收到消息呢..."
            
            # 返回JSON
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps({'reply': reply}, ensure_ascii=False)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8090), ChatHandler)
    print("小七对话服务器启动中...")
    print("访问 http://localhost:8090")
    server.serve_forever()
