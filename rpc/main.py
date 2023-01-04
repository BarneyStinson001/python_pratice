# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json,requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def add(a,b):
    return a+b
# Press the green button in the gutter to run the script.
class School():
    name = 'xindongfang'
    addr = 'shanghai'


class Student():
    name = 'lisi'
    age = '18'
    school= School()
    def to_json():
        json_data={"name":self.name,
                    "company":self.school.name}
        return json.dumps(json_data)


def print_info(student):
    print(f'{student.name} {student.school.name}')
if __name__ == '__main__':
#     print_hi('PyCharm')
#     print(add(5,6))
#     print_info(Student)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#     #22-7 login  validator
#     res=requests.post('http://127.0.0.1:8083/loginJSON',json={
#         "user":"123",
#         })
#     print(res.text)
#     #b'{"error":"Key: \'LoginForm.Password\' Error:Field validation for \'Password\' failed on the \'required\' tag"}'
#     #返回了go语言风格的命名格式，2 英语描述不如中文。

    #22-7  signup validator
#     res=requests.post('http://127.0.0.1:8083/signup',json={
#         "age":130,
#         "name":"joe",
#         "email":"joe@example.com",
#         "password":"password1",
# #         "repassword":"password1",
#     })
# #     print(res.content)#二进制 中文乱码
#     print(res.text)

    #b'{"msg":"ok \xe7\x99\xbb\xe9\x99\x86\xe6\x88\x90\xe5\x8a\x9f"}'
    #乱码  密码怎么没有required  validator 格式错误

    #22-12  请求带token，通过校验
    rsp=requests.get('http://127.0.0.1:8009/ping',headers={
        "x-token":'bob'
    })
    print(rsp.text)



