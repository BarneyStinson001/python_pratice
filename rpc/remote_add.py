# 错误：send_headers  ok :send_header
#错误：self.wfile.send  ok：  self.wfile.write
#错误  ok : import json
#错误 serve_forever()

import json
from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qsl

# 暴露端口
host=('',8003)
class AddHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url=urlparse(self.path)
        qs = dict(parse_qsl(parsed_url.query))
        a = int(qs.get("a",0))
        b = int(qs.get("b",0))
        self.send_response(200)
        self.send_header("content-type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"result":a+b}).encode('utf-8'))

if __name__=='__main__':
    server=HTTPServer(host,AddHandler)
    print('启动')
    server.serve_forever()
