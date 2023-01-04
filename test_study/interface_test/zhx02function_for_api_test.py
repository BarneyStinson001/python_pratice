# coding = utf-8

import requests

import zhx01config

#定义函数，调用函数进行
def test_register():
    r = requests.post(zhx01config.url_register['注册接口'], zhx01config.url_register['params'])
    status = r.status_code
    if status == 200:
        print('状态码检验通过')
    else:
        print('状态码检验不通过')
    print(status)
    print(r.content)


def test_login():
    r = requests.get(url=zhx01config.url_login)  # 接口分离  ，不用去代码里面改接口变量了
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

# 封装get和post函数，传入用例json数据，打印结果，和返回结果
def get(data):
    r=requests.get(data['url'],data['params'])
    if r.status_code == 200:
        data['isok']='ok'
    print(r.content)
    return data

def post(data):
    r = requests.post(data['url'], data['params'])
    if r.status_code == 200:
        data['isok'] = 'ok'
    print(r.content)
    return data


if __name__=='__main__':
    test_register()
    print('test_register done')
    test_login()
    print('test_login done')

