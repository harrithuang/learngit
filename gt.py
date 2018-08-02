import time;
# a=0
# num=1
# while num<=100:
#     a+=num
#     num+=1
#     print(a)
#
# name=input("请输入姓名：")
# if name=='hc':
#    print("1")
# else:
#    print("2")
# if {}:
#     print('1')


# a_list=[1,2,3,4,5]
# print(type(a_list))
# print(len(a_list))
# print(len(a_list)-1)
#-------元组-------tuple
# b_tuple=[1,2,3,4,5]
# b_tuple=(1,)
# print(b_tuple)
# -------列表-----list
# a_list=[1,2,3,[4,5]]
# a_list.append('hc')
# a_list.pop(1)
# a_list.insert(1,'hc')
# a_list[3]='hc'
# print(a_list)
# ---------字典--------dict
# a_dict={'name':'hc','age':'23',"sex":"man"}
# a_dict['house']='100'
# print(a_dict)
# a_dict['name']='baozi'
# print(a_dict)
# a_dict.get('name')
# print(a_dict.get('name'))
# a_dict.pop('name')
# print(a_dict)
# a_dict.popitem()
# print(a_dict)
# a_dict.clear()
# print(a_dict)
# ----组合-----set
# e_set={1,2,3,4,5}
# e_set.add('c')
# # print(e_set)
# # e_set.remove(2)
# # print(e_set)
# e_set.update([1,2,3,6])
# print(e_set)
# ---if elif---------
# age=5
# if age<=6:
#     print('kid')
# elif age<=18:
#     print('teenager')
# else:
#     print('adult')

# a=float(input("请输入体重："))
# b=float(input("请输入身高："))
#
# if a < 2.0 and b<50:
#     print('教主')
# elif a>1.7 and b>60:
#     print('教皇')
# else:
#     print('平民')

# a=range(10)
# print(type(a))
# print(list(a))
#------rang函数-------
# for x in range(1,22,5):
#     print(x)

# x=range(9)
# print(type(x))
# print(list(x))
# a=0
# for n in range(1,100):
#     if n%2!=0:
#         a+=n
#         print(a)
# ----字典-----dict
# a_dict={'name':'harrit','age':'23'}
# for key,value in a_dict.items():
#     print(key)
#     print(value)
#-----while循环--------
# n=1
# while True:
#     print(n)
#     n+=1
#     if n>=10:
#       break
# a_list=['Bart', 'Lisa', 'Adam']
# for value in a_list:
#     print('hello',value)

# for letter in 'Python':
#     print('当前字母：',letter)

# n=0
# while n<10:
#     n=n+1
#     if n%2==0:
#         continue
#     print(n)
#-----for循环-------
# for letter in 'harrit':
#     if letter=='i':
#         pass
#         print('666')
#     print('当前字母是：'),letter
#-----时间参数--------
# ticks=time.time()
# print(ticks)
# localtime=time.ctime()
# print(localtime)
#-----通过instance（x，x1）判断类型----
# def make(age):
#     if isinstance(age,float):
#         return abs(round(age))
#     if not isinstance(age,int):
#         raise TypeError('调用参数类型输入错误')
#     if isinstance(age,int):
#         if age<0:
#             return abs(age)
#         else:
#             return age
#
# age=make(55)
# print(age)
#----不定长函数的-----
# def get_num(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     print(sum)
#     return sum
# get_num(1,2,3,4)


#----导入函数方法包----
# import math
# a=dir(math)
# print(a)

# ----全局变量-----
# Money = 2000
# def AddMoney():
#     # 想改正代码就取消以下注释:
#     global Money (全局变量)
#     Money = Money + 1
# print(Money)
# AddMoney()
# print(Money)
# -------文件的读写--------
# import os
# f=open('C:/Users/sdsf/Desktop/study file.txt','w+',encoding='utf-8')
# f.write('cool man')
# print(f.read())
# f.close()
# -------文件的读写----
# import os
# with open('C:/Users/sdsf/Desktop/study file.txt','w+',encoding='utf-8') as f:
#     print(f.write('7/17 \nI/O文件读写：Open(filepath,"读写方法"),\n也可以直接用with open()as f 省略了close（）的调用。'))
# a=[]
# for b in range(1,11):
#     a.append(b*b)
# print(a)
# --索引---
# l=[(1),(2),3]
# print(l.index(3))

#-----迭代器-----
# from collections import Iterator
# isinstance((x for x in range(10)),Iterator)
# True
# print( isinstance([], Iterator))
# False
# print( isinstance({}, Iterator))
# False
# print( isinstance('abc', Iterator))


#-------类---------
# class Student(object):
#     def __init__(self,_name,_score):
#         self._name = _name
#         self._score = _score
#     def test(self):
#         if self._score>=90:
#             print("成绩为：A")
#         elif 60<=self._score<90:
#             print("成绩为：B")
#         elif self._score<60:
#             print("成绩为：C")
#         else:
#             print("成绩分数不存在")
#
#         return
# cc = Student('harrit',20)
# cc.test()
#----继承--------
# class Animal(object):
#     def run(self):
#         print('animal is running')
# class Dog(Animal):
#     pass
# class Pig(Animal):
#     pass
# dog=Dog()
# pig=Pig()
# dog.run()
# pig.run()
# -----多态--------
# class Animal(object):
#     def f1(self):
#      if isinstance(Dog,Animal):
#         print(True)
#      elif isinstance(Pig,Animal):
#         print(True)
#      else:
#          print(False)
# class Dog(Animal):
#     pass
# class Pig(Animal):
#     pass
# d=Dog()
# p=Pig()
# d.f1()
# p.f1()
# -------类的属性优先级低于实例属性--------
# class Student(object):
#     def test(self,name):
#         self.name=name
# s=Student()
# s.test('tt')
# s.name='taozi'
# print(s.name)

# ------写这个犯了2个错误，一个是输出时候忘记格式化了,%s,%d,第二个是要初始化，调用方法的时候先把类这一层打开在调用方法--
# class Man(object):
#     def __init__(self,name,age,weight,height):
#         self.name=name
#         self.age=age
#         self.weight=weight
#         self.height=height
#     def shuxing(self):
#      print("这位帅哥的信息：姓名：%s,年龄：%d，体重：%d，身高：%d"%(self.name,self.age,self.weight,self.height))
# a=Man('harrit',23,55,172)
# a.shuxing()


# ----slots---------有待改正
# class  Tao(object):
#     def __init__(self,eating,sleeping):
#         self.eating=eating
#         self.sleeping=sleeping
#     def jineng(self):
#      print("我会的技能有：%s,%s"%(self.sleeping,self.eating))
# a=Tao("吃饭","睡觉")
# a.jineng()

# -------多重继承--------
# class grandpa(object):
#     def play1(self):
#         print("我是你爷爷")
# class grandmo(object):
#     def play2(self):
#         print("我是你奶奶")
# class MF(grandmo,grandpa):
#     def play3(self):
#         pass
# class son(MF):
#     def play4(self):
#         pass
# if __name__ == '__main__':
#     s=son()
#     s.play1()
# # ----------枚举类-----------
# from enum import Enum, unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')



# class Teacher(object):
#   def __init__(self,write,study,read):
#     self.write = write
#     self.study = study
#     self.read = read
# class Student(Teacher):
#     def oprate(self):
#      print("我会的技能有：%s,%s,%s"%(self.write,self.study,self.read))
# ww =Student('写字','学习','阅读')
# ww.oprate()

# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
#
#
# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)
# getattr(emp1)


# -------------SQLite3 数据库------------------
#
# import sqlite3
# conn=sqlite3.connect('test.db')
# cursor=conn.curson()
# cursor.execute('create table user(id varchar(20)PRIMARY KEY ,NAME VARCHAR (20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# def get_score_in(low, high):
#     ' 返回指定分数区间的名字，按分数从低到高排序 '
#     conn1 = sqlite3.connect(db_file)
#     with conn1:
#         cursor1 = conn1.cursor()
#         cursor1.execute('select name from user where score >= ? and score <= ? order by score', (low, high))
#         data = cursor1.fetchall()
#         cursor1.close()
#         return [a[0] for a in data]


# -------网络爬虫------------
# import requests
# from bs4 import BeautifulSoup
# response=requests.get(url='https://www.autohome.com.cn/all/')
# response.encoding=response.apparent_encoding
# print(response.text)
# soup=BeautifulSoup(response.text,features='html.parser')
# target=soup.find(id='sidebarWrap')



















