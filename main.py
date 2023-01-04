# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json,requests,locust

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class MyUser(locust.HttpUser):
    wait_time = locust.between(1,2)

    @locust.task
    def test_api(self):
        rsp = self.client.get('http://127.0.0.1:8003/?a=1&b=2')
        print(rsp.text)
        assert json.loads(rsp.text).get('result')==3



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    rsp = requests.get('http://127.0.0.1:8003/?a=1&b=2')
    print(rsp.text)
    assert json.loads(rsp.text).get('result')==3

    rsp =requests.get('http://127.0.0.1:8003/get_mpd')
    print(rsp.text)
    assert rsp.json()['result']=='asddsfdsfsdf:dsdd\ndfsfdsfd\ndvgvfdvfd\n'

    rsp =requests.get('http://127.0.0.1:8003/get_slice')
    print(rsp.text)
    assert rsp.json()['result']=='slice............'


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

