# coding =utf-8
# 引入模块
import requests
# 引入配置文件
import zhx01config

r = requests.get(url=zhx01config.url_home)  # 接口分离  ，不用去代码里面改接口变量了
status = r.status_code
if status == 200:
    print('状态码检验通过')
else:
    print('状态码检验不通过')
print(status)

j = r.json()
if '裤子女夏' in str(j):
    print('存在此数据')
else:
    print('不存在此数据')
print(j)

# post的参数也要分离出去
r = requests.post(zhx01config.url_register['注册接口'], zhx01config.url_register['params'])
status = r.status_code
if status == 200:
    print('状态码检验通过')
else:
    print('状态码检验不通过')
print(status)
print(r.content)
