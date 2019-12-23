# class Father(): #声明父类
#     def __init__(self,a,b):#给类设置属性
#         self.a=a
#         self.b=b
#         #方法一
#         def add(self):# 类的方法add
#          return self.a+self.b
#         #方法二
#         def sub(self):
#             return self.a - self.b
# class Son(Father):#声明子类继承父类
#       def print_add(self):
#           #调用父类的方法
#           print(self.add())
#           #重写父类的方法
#           def sub(self):
#               #调用父类的属性
#               return self.a*2-self.b
# son=Son(6,3)
# son.sub()
# son.add()
#  类的属性和方法练习：
# 写一个学生类
# 写出学生应该有的属性和方法
# class Student():
#     def __init__(self,name,age,sid,hobby):
#         self.name=name
#         self.age=age
#         self.sid=sid
#         self.hobby=hobby
#     def study(self):
#             print("%s同学是个优秀的学习委员他今年%d学号是%d他的爱好是%s"%(self.name,self.age,self.sid,self.hobby))
# s1 = Student("小强",18,101,"学习")
# s1.study()
# 2. 继承
# 写一个人类类
# 再写一个学生类
# 学生类继承人类的属性和方法
# class Person():
#        def __init__(self,name,age):
#            self.name=name
#            self.age=age
#        def func(self):
#             return "%s今年%d喜欢插花" % (self.name,self.age)
#        def work(self,work):
#            return "他的工作是%s" % (work)
# p=Person("张三",18)
# x=p.work("测试")
# print(x)
# class Student(Person):
#     def __init__(self,name,age,con):
#         Person.__init__(self,name,age)
#         self.con=con
#     def print_func(self):
#         x=self.func()
#         print(x)
#     def sfunc(self,name,age):
#        return "%s今年%d班里一支花"%(name,age)
#
# s=Student("小红",18,"五班")
# #s.print_func()
# s1=s.sfunc("小黄",22)
# print(s1)
#3. 定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key，并返回删除后的字典
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})
#创建一字典类
# class Dictclass():
#     #设置类的属性(这里的属性是一个字典)
#     def __init__(self,dict):
#         self.dict=dict
#     #定义删除key的方法如果调用这个函数需要传一个字典(实例化类需要一个字典)和一个key进来
#     def del_dict(self,key):
#         #如果传进来的key在字典里面
#         if key in self.dict.keys():#kyes()以列表返回一个字典所有的键
#             #删除这个键对应的值
#             del self.dict[key]
#             #返回删除后的字典
#             return self.dict
#         else:
#             #如果字典里没有对应的key则返回这句话
#             return "this dict don't have this key"
#     #获取键对应的字典的方法
#     def get_dict(self,key):
#         # 如果key在字典里面
#         if key in self.dict.keys():
#             #将键对应的值返回
#             return self.dict[key]
#         else:
#             # 如果字典里没有对应的key就返回没找到
#             return "not found"
#     #返回键组成的列表：返回类型;(list)
#     def get_key(self,key):
#         # 如果key在字典里面
#         if key in self.dict.keys():
#             #返回键组成的列表
#             return self.dict.keys
#
#     def update_dict(self,dict2):
#         self.dict.update(dict2)
#         return self.dict
# #创建一个字典
# dict1={'name':'小白','age':18,'hobby':'电影','sex':'男'}
# #创建第二个字典
# dict2={'id':'9527'}
# #实例化字典类
# d1=Dictclass(dict1)
# d1.del_dict('name')
# print(dict1)
# d2=d1.get_dict('age')
# print(d2)
# d3=d1.get_key("sex")
# print(d3)
# d4=d1.update_dict(dict2)
# print(d4)