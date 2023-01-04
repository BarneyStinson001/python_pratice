import time#可以导入其他包
from locust import HttpUser, task, between


#定义类，模仿用户，有个属性client
#压力测试时,每个用户一个实例
#必须要有一个类继承自User
class QuickstartUser(HttpUser):#HttpUser不能

    #wait_time属性：每个任务间的间隔
    wait_time = between(1, 5)

    # 每个用户，lcust创建协程进行调用任务。
    @task
    def hello_world(self):
        #自定义请求和响应
        self.client.get("/hello")
        self.client.get("/world")

    #任务权重
    @task(3)
    def view_items(self):
        for item_id in range(10):
        #用了参数化的方法，但不会分开统计
        #根据url进行分组，不同商品不会分开统计
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    #类似于初始化：例子登录
    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})