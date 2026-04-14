#!/usr/bin/env python3
# 星契塔罗服务器
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

PORT = 8083
DIR = r"C:\.openclaw\workspace\pet\star-tarot"

class TarotsHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_POST(self):
        if self.path == '/chat':
            # AI解读功能 - 调用星座馆API
            import urllib.request, json
            
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            # 简单转发到星座馆服务器
            data = urllib.parse.parse_qs(post_data)
            message = data.get('message', [''])[0]
            
            api_url = 'http://127.0.0.1:8090/chat'
            req_data = json.dumps({'message': message}).encode('utf-8')
            req = urllib.request.Request(api_url, data=req_data, headers={'Content-Type': 'application/json'})
            
            try:
                r = urllib.request.urlopen(req, timeout=30)
                resp = json.loads(r.read().decode('utf-8'))
                reply = resp.get('reply', '小七暂时无法回应')
            except:
                reply = '小七暂时无法回应，请稍后再试。'
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'reply': reply}).encode('utf-8'))
        else:
            self.send_error(404)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', PORT), TarotsHandler)
    print(f"星契塔罗服务器启动成功！")
    print(f"访问: http://localhost:{PORT}")
    server.serve_forever()
