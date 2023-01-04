# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from peewee import *
import datetime
import logging
from peewee_test.model_define import Man,User,Tweet,Favorite


#打印sql语句
logger =logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
db = MySQLDatabase('peewee_test',host ='127.0.0.1',user='root',passwd='009988')


def populate_test_data():
    db.create_tables([User, Tweet, Favorite])

    data = (
        ('huey', ('meow', 'hiss', 'purr')),
        ('mickey', ('woof', 'whine')),
        ('zaizee', ()))
    for username, tweets in data:
        user = User.create(username=username)
        for tweet in tweets:
            Tweet.create(user=user, message=tweet)

    # Populate a few favorites for our users, such that:
    favorite_data = (
        ('huey', ['whine']),
        ('mickey', ['purr']),
        ('zaizee', ['meow', 'purr']))
    for username, favorites in favorite_data:
        user = User.get(User.username == username)
        for content in favorites:
            tweet = Tweet.get(Tweet.message == content)
            Favorite.create(user=user, tweet=tweet)



if __name__=='__main__':
    db.connect()
#     db.create_tables([User,Tweet,Favorite])
    #条件查询，and  or
#     man = Man.select().where((Man.first=="li"|Man.first=="v11"))
#     print(man.sql())
#     print(man[:])

    #模糊查询  like      #startswith  endswith
#     man1 = Man.select().where(Man.first.contains('v'))
#     print(man1.sql())
#     print(man1[:])
    #in 查询
    #.in=  <<
#     man2 = Man.select().where(Man.first.startswith('v')).dicts()
#     for a in man2 :
#         print(type(a))
#         print(a)

    #排序 limit 去重
#     print("排序")
#     query=(Man.select().order_by(Man.first.desc()).limit(3).distinct())
#     #query=(Man.select().order_by(-Man.first).limit(3).distinct())#符号等价逆序
#     print(query.sql())
#     print(query[:])
#     print(query[0])
#     print(query[0].add_time)

    #count()
#     print(Man.select().order_by(Man.first.desc()).limit(3).distinct().count())

    #聚合函数，子查询，分页计数。外键，多表查询
#     query=Man.select(fn.MAX(Man.first)).execute()#未查询要execute
#     print(query)#<peewee.ModelObjectCursorWrapper object at 0x0000018A317B84C0>
#     query=Man.select(fn.MAX(Man.first)).scalar()#未查询要execute
#     print(query)
#
#
#     user = Man.select().where(Man.first==query)
#     for a in user:
#         print(type(a))#<Model: Man>
    #用子查询。查询最大值
    #select user.name from user where age = (select max(age) from user)
#     sub_query=Man.select(fn.MAX(Man.first))
#     query = Man.select(Man.first).where(Man.first==sub_query)
#     for a in query:
#         print(a)


    #分页和统计

    #执行原生sql
#     query = Man.raw('select * from man where first = %s',"li")#不需要双引号
#     for a in query:
#         print(a)
#     query = Man.select().where(SQL('first = "%s"'% "li"))#需要双引号
#     for a in query:
#         print(a)
#
#     # 查询多条
#     man = Man.select()
#     print(man.sql())
#     for a in man:
#         print(a)

    #表连接join
        #用户  推特  user喜换tweet

#     造数据
#     populate_test_data()

    #推文作者
#     for a in Tweet.select():
#         print(a.message,a.user.username)

    #表连接，推文喜欢的人
    #select * from tweet join favorite on tweet.id=favorite.tweet_id
    #query= Tweet.select(Tweet,Favorite).join(Favorite).where(Tweet.user_id=="mickey")
    query= Tweet.select(Tweet,Favorite).join(Favorite,on=(Tweet.id==Favorite.tweet_id)).where(Tweet.user_id=="mickey")
    #print(query.sql())
    for  a in query:
        print(a.message,a.user_id)
#
#     #外键  反向取
#     user= User.get(User.username=='mickey')
#     tweets= Tweet.select().where(Tweet.user_id==user)
#     for a in tweets:
#         print(user.username,a.message)
#     #反向2
#     tweets= User.get(User.username=='mickey').tweets
#     for a in tweets:
#         print(user.username,a.message)

    #性能问题,想得到五个数据。发起五次请求+1次
    print('多一次查询')
    for tweet in Tweet.select():
        print(tweet.message,tweet.user.username)
    #join操作，改成一次查询
    query = Tweet.select(Tweet,User.username).join(User).where(User.username=='mickey')
    for a in query:
        print(a.user.username,a.message)

    #什么时候发起sql请求，会发起多少次请求，高手不会喜欢用orm。不灵活。