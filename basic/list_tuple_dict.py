
from genericpath import samefile
import imp
from operator import itemgetter
import random
from turtle import st


# 2-1 如何在列表、字典、集合中根据条件筛选数据：
# 列表中的负数。分数大于90的学生。被3整除的元素
# 列表、字典、集合解析式
list1=[random.randint(-5,5) for _  in range(10)]
print(list1)
ans1=[x for x in list1 if x <0]
print(ans1)


dict1={'student%d'%i:random.randint(60,100) for i in range(10)}
print (dict1)
print({k:v for k,v in dict1.items() if v>=90 })
print({item[0]:item[1] for item in dict1.items() if item[1]>=90 })
print(dict(filter(lambda x:x[1]>=90,dict1.items())))

set1={random.randint(1,20) for _ in range(10)}
print(set1)
print(set(x for x in set1 if x%3==0))

# 元祖命名，提高程序可读性
# 元素比字典省空间，如果是固定格式，可采用set
# NAME = 0
# AGE = 1
# GENDER = 2
# EMAIL = 3
# 元祖拆包
NAME,AGE,GENDER,EMAIL = range(4)
student1 = ('lisi',20,'male','111@222.com')
print('studeng: name %s\n  age: %d\n  gengder: %s\n  email: %s\n'%(student1[NAME],student1[AGE],student1[GENDER],student1[EMAIL]))
#枚举
from enum import IntEnum
class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    GENDER = 2
    EMAIL = 3
print('studeng: name %s\n  age: %d\n  gengder: %s\n  email: %s\n'%(student1[StudentEnum.NAME],student1[StudentEnum.AGE],student1[StudentEnum.GENDER],student1[StudentEnum.EMAIL]))

#collcections.nametuple
from collections import namedtuple
Student=namedtuple('student',['name','age','sex','email'])
s1=Student('lisi',20,'male','111@222.com')
print('studeng: name %s\n  age: %d\n  gengder: %s\n  email: %s\n'%(s1[0],s1[1],s1.sex,s1.email))


#2-3 根据字典值对项排序
scores = {k:random.randint(50,100) for k in 'abcdefgh'}
print(scores)
d = {(v,k) for k,v in scores.items()}
print(d)
print(sorted(d,reverse=True))

#2-4 统计序列中的元素频率

#2-5 找到多个字典中的公共键  每轮都有进球：
#1、构建每轮进球人
d1 = {k:random.randint(1,4) for k in random.sample('abcdefghi',random.randint(3,6))}
d2 = {k:random.randint(1,4) for k in random.sample('abcdefghi',random.randint(3,6))}
d3 = {k:random.randint(1,4) for k in random.sample('abcdefghi',random.randint(3,6))}
print(d1,d2,d3)
for i in d1.keys():
     if i in d2 and i in d3:
         print(i)
         
print([i for i in d1 if i in d2 and i in d3])

