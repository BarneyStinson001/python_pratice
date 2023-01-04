# 常见错误：未导入json

import requests,json


#http调用
#每个都需要记住url地址，参数传递，返回数据解析
rsp = requests.get('http://127.0.0.1:8003/?a=1&b=2')
print(rsp.text)

# 如何像本地函数调用一样：
class Client():
    def __init__(self,url):
        self.url=url
    def add(self,a,b):
        rsp = requests.get(f"{self.url}/?a={a}&b={b}")
        return json.loads(rsp.text).get("result",0)

client=Client('http://127.0.0.1:8003')
print(client.add(3,4))