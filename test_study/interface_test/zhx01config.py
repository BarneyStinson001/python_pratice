# coding =utf-8
# 主要存放接口

# baseurl 一般接口都是分测试接口和正式接口的，只需要修改ip即可
baseurl = 'http://suggest.taobao.com'
# 假设下面三个接口
url_login = baseurl + '/sug?code=utf-8&q=裤子&callback=cb 用例'
# url_register=baseurl+'/sug?code=utf-8&q=裤子&callback=cb 用例'
url_register = {'注册接口': baseurl + '/sug?', 'params': {'code': 'utf-8', 'q': '裤子', 'callback': 'cb'}}

url_home = baseurl + '/sug?code=utf-8&q=裤子&callback=cb 用例'

"""
title:用例的名称
condition:前置条件，写skip跳过这条用例
url:接口的链接
params：参数 如果是headers 就增加一个headers   # 接口需要传入编码格式   搜索条件 如 裤子等信息
type:请求类型 get post put 等等 请求的类型 get 就写get  post就写post
isok：用例是否通过         用例等待的时间 秒 1就是等待1秒后执行
time：这条用例是否需要等待  用例等待的时间 秒 1就是等待1秒后执行
"""


# 中级一、用例封装
httpurl_date=[
    {'title':'注册接口','condition':'','url':'{}/sug?'.format(baseurl),'params':{'code': 'utf-8', 'q': '裤子', 'callback': 'cb'},'type':'get','isok':'','time':'1'},
    {'title': '登录接口', 'condition': '', 'url': '{}/sug?'.format(baseurl), 'params':{'code': 'utf-8', 'q': '裤子', 'callback': 'cb'}, 'type': 'post', 'isok': '', 'time': ''},
]