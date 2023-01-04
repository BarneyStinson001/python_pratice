import locust,time

urls=['/?a=1&b=2']

class DASH_live_task(locust.SequentialTaskSet):
    def  on_start(self):
        with self.client.get(urls[0]) as rsp:
            self.rsp=rsp.json()
            print(self.rsp.items())
    @locust.task
    def parse_mpd(self):
        time.sleep(2)
        print(self.rsp.keys())
        # with self.client.get(self.refresh_url) as rsp:
        #     self.audio_list=rsp.text
        #     self.video_list=rsp.text
    @locust.task
    def get_last_audio(self):
        time.sleep(2)
        print("get from mpd "+str(self.rsp['result']))
        # with self.client.get(self.audio_list[0]) as rsp:
        #     if rsp.statuscode >=400:
        #         rsp.failue("req failed")

class DASHPlayer(locust.HttpUser):
    tasks = [DASH_live_task] #任务控制，顺序拉取索和分片
    locust.constant_pacing(3)#每秒拉一次索引
    # host = 'http://127.0.0.1:8003'
    # wait_time = locust.constant_pacing(6)



