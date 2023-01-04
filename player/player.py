#! conding=utf-8
# 有三个用户，dash  hls mss
# 两个播放
#   类点播：点播 tvod
#   类直播：live  tstv

# 开闭原则
# 写好的类尽量不修改里面的内容

class Player():
    def get_index(self):
        pass

    def get_slice(self):
        pass


# 其实可以不用,还是要的。
class DashPlayer(Player):
    def get_index(self):
        print("dash mpd is ")

    def get_slice(self):
        print("dash m4s is ")


class HlsPlayer(Player):
    def get_index(self):
        print("hls m3u8 is ")

    def get_sec_index(self):
        print("hls second m3u8 is ")

    def get_slice(self):
        print("hls ts is ")


class MssPlayer(Player):
    def get_index(self):
        print("dash manifest is ")

    def get_slice(self):
        print("dash m4s is ")


# 简单工厂
# 缺点：新增后，需要修改工厂类的map ，违背开闭原则 --“一个类写好后，尽量不要修改里面的内容”
class PlayerFactory():
    def create_leifeng(self, type):
        map_ = {
            "dash": DashPlayer(),
            "hls": HlsPlayer(),
            "mss": MssPlayer()
        }
        return map_[type]


# 工厂方法
# 需要增加一个中学生类和一个中学生工厂类（MiddleStudentFactory），虽然比较繁琐，但是符合封闭开放原则
# 在工厂方法中，将判断输入的类型，返回相应的类这个过程从工厂类中移到了客户端中实现，
# 所以当需要新增类是，也是要修改代码的，不过是改客户端的代码而不是工厂类的代码。

class NewPlayerFactory():
    def create_player(self):
        pass


class DashPlayerFactory(NewPlayerFactory):
    def create_player(self):
        return DashPlayer()


class HlsPlayerFactory(NewPlayerFactory):
    def create_player(self):
        return HlsPlayer()


class MssPlayerFactory(NewPlayerFactory):
    def create_player(self):
        return MssPlayer()


if __name__ == '__main__':
    p1 = PlayerFactory().create_leifeng("dash")
    p1.get_index()
    p1.get_slice()
    p2 = PlayerFactory().create_leifeng("hls")
    p2.get_index()
    p2.get_slice()
    p3 = PlayerFactory().create_leifeng("mss")
    p3.get_index()
    p3.get_slice()

    myPlayerFactory=DashPlayerFactory()
    dash1=myPlayerFactory.create_player()
    dash2=myPlayerFactory.create_player()
    dash1.get_index()
    dash2.get_slice()
