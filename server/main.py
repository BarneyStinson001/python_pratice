import socket
import sys
import re
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

root_dir='C:\\Users\\zhuhangxin\\PycharmProjects\\zhxtestproject'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    #1、创建套接字
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #指定运行方式  python main.pi xxxx
    if len(sys.argv)==2:
        port = sys.argv[1]
    else:
        print("运行方式如：python main.py  xxxx")
        return
    print("您使用的端口为%s"%port)   #增加提示信息
    #2、绑定本地信息
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(("",int(port))) #类型转换
    #3、变为监听套接字
    server_socket.listen(128)
    #4、等待对方连接

    while True:
        new_socket,new_addr= server_socket.accept()

        #5、接收数据
        request = new_socket.recv(1024).decode('utf-8')
        request_lines= request.splitlines()
#         for i,line in enumerate(request_lines):
#             print(i,line)
        #提取请求的文件
        res=re.match(r"([^/]*)([^ ]*)",request_lines[0])
        print(res.group(2))
        filename=res.group(2)
        if filename=='/':
            filename='index.html'
        try:
            f = open(root_dir+filename,"rb")# 图片二进制读取
        except:
            response_header='HTTP/1.1 404 NOt Found\r\n'
            response_header+='Content-Type: text/html;charset=utf-8\r\n'
            response_header+='\r\n'
            response_body='file not found ,请输出正确的url'#乱码需要在响应头里加上Content-Type

            new_socket.send(response_header.encode('utf-8'))
            new_socket.send(response_body.encode('utf-8'))
        else:
            content=f.read()#文件不大的情况，直接读
            #读取数据
            response_header="HTTP/1.1 200 OK \r\n"#反斜杠转义  不是/n
            response_header+="\r\n"
            response_body = content
    #         response = response_header+response_body
    #         print(response)
            #将数据返回给浏览器
    #         new_socket.send(response.encode('utf-8'))
            #分开返回响应头和响应体，二进制文件不用encode
            new_socket.send(response_header.encode('utf-8'))
            new_socket.send(response_body)
            f.close
        finally:
            #关闭套接字
            new_socket.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
