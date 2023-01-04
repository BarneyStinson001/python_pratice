# coding =utf-8
import requests,zhx01config

# 请求方法为get,需要在url体现参数字段和相应值
url = 'http://suggest.taobao.com/sug?code=utf-8&q=裤子&callback=cb 用例'
r = requests.get(url=url)
status = r.status_code
print(status)
j = r.json()
print(j)

# 请求方法为post,参数通过字典传入
url = 'http://suggest.taobao.com/sug'
data = {'code': "utf-8", 'q': '裤子', 'callback': 'cb 用例'}
r = requests.post(url=url, data=data)
status = r.status_code
print(status)
j = r.content  # content不是content（），不是callable
print(j)

# 接口状态码断言，和响应消息体正异常断言：
url = 'http://suggest.taobao.com/sug?code=utf-8&q=裤子&callback=cb 用例'
r = requests.get(url=url)
status = r.status_code
print(status)
j = r.json()
print(j)
if status == 200:
    print('状态码验证通过')
else:
    print('状态码验证不通过')

if '裤子女夏' in str(j):
    print('存在数据')
else:
    print('不存在此数据')

if '裤子女夏2' in str(j):
    print('存在数据')
else:
    print('不存在此数据')
