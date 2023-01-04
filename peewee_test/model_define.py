# coding=utf-8

from peewee import *
import datetime
import logging

#打印sql语句
logger =logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


db = MySQLDatabase('peewee_test',host ='127.0.0.1',user='root',passwd='009988')


#功能字段  公共字段
class BaseModel(Model):
    add_time = DateTimeField(default=datetime.datetime.now(),verbose_name="添加时间")
    class Meta:
        database=db

class Person(BaseModel):
    name = CharField(verbose_name="姓名",max_length=10,null=False,index=True)
    passwd = CharField(verbose_name='密码',max_length=20,null=False,default='123456')
    email= CharField(verbose_name='邮箱',max_length=50,null=False,unique=True)
    gender= IntegerField(verbose_name='性别',null=False,default=1)
    birthday = DateField(verbose_name='生日',null=True,default=None)
    is_admin = BooleanField(verbose_name='是否是管理员',default=True)
    class Meta:
#         database=db#可以继承
        table_name = 'persons' #指定表名


class User(Model):
    username = CharField(primary_key=True,max_length=20)#类型
    #没有设置主键，则自动生成主键。如果用primary_key=True则可以不用unique=True
    age= CharField(default=18,max_length=20,verbose_name="年龄" )
    class Meta:
        database = db#数据库

class Tweet(Model):
    user = ForeignKeyField(User, backref='tweets')#外键类型，一用户多tweets,反向查询
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

    class Meta:
        database = db

class Favorite(BaseModel):
    user = ForeignKeyField(User,backref='favorites')
    tweet  =  ForeignKeyField(Tweet,backref='favorites')

#联合索引
class Man(BaseModel):
    first=CharField()
    last = CharField()
    class Meta:
        primary_key=CompositeKey('first','last')

#约束 联合主键的外键
class Pet(BaseModel ):
    owner_first =CharField()
    owner_last = CharField()
    pet_name = CharField()

    class Meta:
        constraints =[SQL('FOREIGN KEY(owner_first,owner_last) REFERENCES man(first,last)')]

class Blog(BaseModel):
    pass
class Tag(BaseModel):
    pass

#复合主键
class BlogToTag(BaseModel):
    #多对多关系
    blog = ForeignKeyField(Blog)
    tag  = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('blog','tag')

#
# if __name__=='__main__':
# #1、生成表
#     db.connect()
#     db.create_tables([User,Tweet,Person,Man,Blog,Tag,BlogToTag,Pet])
#
# #2、添加数据 save  create
#     charlie = User(username="charlie")  #update  set age = 18 where username= ''
#     rows=charlie.save()#新建或者更新。内部逻辑（是否有设置主键，带主键就会更新操作。update语句,但没有其他项可以更新）
#     if(rows==0):
#         print("未更新数据")
# #
# #     #charlie.save(force_insert=True)#"Duplicate entry 'charlie' for key 'user.user_username'")
# #     Mike= User.create(username='mike')#直接用User的create方法
#
#
#
# #3、查询
# #     charlie = User.get(User.username=='charlie')
# #     print(charlie.username)
#     #查询不到,会抛出异常。UserDoesNotExist
#
#     try:
#         charlie = User.get_by_id("charlie")#charlie不是id所以查询不到
#         print('=====0')
#         print(charlie.username)
#         print('=====0')
#         Ellie= User.get(User.username=='Ellie')
#     except User.DoesNotExist as e:
#         print('查询不到')
# #     print(Ellie.username)
#
#     #select操作
#     users = User.select()
#     print(type(users))#没有查询
#     print(users.sql())#组装了sql
#     #循环和切片才有查询操作
#     print('===1')
#     usera=users[0]
#     print(type(usera))#没有查询
#
#     for user in User.select():
#         print(user.username)
# #     print('===')
# #     #where 语句 in查询
# #     usernames = ['alice','mike','charlie']
# #     users = User.select().where(User.username.in_(usernames))
# #     for user in users:
# #         print(user.username)
#
#  #更新    save逻辑：update set xx=xx where username = xxx
#
# #     charlie=User.create(username='charlie')
# #     print(charlie.save())
#     #使用update
# #     print(User.update(age=20).where(User.username=="charlie").execute())
#
# #删除
#     #get直接操作
# #     user= User.get(User.username=="mike")
# #     user.delete_instance()
# #
# #     #返回sql语句，不执行。要调用execute()
# #     query = User.delete().where(User.username=="charlie").execute()
# #     print(query)
#
# #更多操作
# # 抽取到BaseModel，继承
#
# # 主键和约束
#
#
#
# # primary_id = Man.insert({'first':'li','last':'si'}).execute()
# # print(primary_id)
# primary_id = Blog.insert({}).execute()#不会自动生成
# print(primary_id)
#
# blog =Blog()
# print(blog.id)#None
# blog.save()#没有设置值，就会使用默认值
# print(blog.id)#数据库返回的。
#
#
# # data_source= [
# # {'first':"v11",'last':'v21'},
# # {'first':"v12",'last':'v22'}
# # ]
# # for data_dict in data_source:
# #     Man.create(**data_dict)#性能差
#
# data_source= [
# {'first':"v13",'last':'v23'},
# {'first':"v14",'last':'v24'}
# ]
# query=Man.insert_many(data_source).execute()
# print(query)

