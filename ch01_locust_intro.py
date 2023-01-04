# 204 定义接口
# 路径 相同的的部分  :6410/003/2/
def init(user):
    user.client.get('/?a=0&b=0')


def init2(user):
    user.client.get('/?a=1&b=1')


def get_mpd(user):
    user.client.get('/get_mpd')


def get_slice(user):
    user.client.get('/get_slice')


# 205  定义任务集
from locust import TaskSet


class dash_live_behavior(TaskSet):  # 自定义用户行为
    tasks = {get_mpd: 1, get_slice: 1}

    # task属性  设置哪些接口和权重
    def on_start(self):
        print('start_user_task: dash_live')
        # 获取到重定向地址，后面拿来用
        init(self)

    def on_stop(self):
        init2(self)
        print('stop_user_task: dash_live')


class dash_vod_behavior(TaskSet):
    tasks = [get_slice]  # 索引文件在on_start拉

    def on_start(self):
        print('start_user_task: dash_vod')
        init(self)
    def on_stop(self):
        init(self)
        print('stop_user_task: dash_vod')


class hls_vod_behavior(TaskSet):
    tasks = [get_slice]

    def on_start(self):
        print('start_user_task: hls_vod')
        init(self)
        init2(self)

    def on_stop(self):
        print('stop_user_task: hls_vod')


class hls_live_behavior(TaskSet):
    tasks = [get_mpd, get_slice]

    def on_start(self):
        print('user_task: hls_live')
        init(self)
        init2(self)

    def on_stop(self):
        print('user_task: hls_live')


# python库   unittest  jmeter  robotframework   都相似  init  setup   teardown

# 206  定义用户类

host = 'http://127.0.0.1:8003'
from locust import HttpUser,constant


class dash_vod_player(HttpUser):
    tasks = [dash_vod_behavior]
    host = host
    weight = 1
    wait_time = constant(1)


class dash_live_player(HttpUser):
    tasks = [dash_live_behavior]
    host = host
    weight = 1
    wait_time = constant(1)

#
#
# class hls_vod_player(HttpUser):
#     tasks = [hls_vod_behavior]
#     host = host
#     weight = 1
#     wait_time = constant(1)
#
#
# class hls_live_player(HttpUser):
#     tasks = [hls_live_behavior]
#     host = host
#     weight = 1
#     wait_time = constant(1)
