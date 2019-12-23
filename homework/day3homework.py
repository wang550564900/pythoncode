# 1. 有这样一种数如：12321（第一个等于最后一个，
# 第二个等于倒数第二个，以此类推，直到中间仅剩一个数），
# 写一个函数，传入一个整数，判断这个数是不是这种前后一样的数。
#lst="12346764321"
# num=input("输入一个整数")
# if len(num)>=3 and len(num)%2==1 and num.isdigit():
#     for i in range(len(num)//2):
#         if num[i]!=num[-i-1]:
#             print("这不是一个镜像数")
#             break
#     else:
#         print("这是一个镜像数")
# else:
#     print("输入不合法")

# 2.有这样一个矩阵，设计一个函数，
# 根据我输入的参数，返回其所在的位置是几行几列
#[[3,8 ,9],[6,11,2],[7,18,5]]
# lst=[[3,8 ,9],[6,11,2],[7,18,5]]
# num=input("请输入参数")
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         if int(num)==lst[i][j]:
#             print("输入参数为第%d行,第%d列"%(i+1,j+1))
# # 3.实现登录，账号名为admin，密码123，
# 则提示“登录成功”，如果账号或者密码错误，
# 则提示“账号名或密码错误”
# 并允许重新输入用户名和密码，如果3次登录失败，则提示“登录失败”并退出程序。
# for i in range(0,3):
#      username="admin"
#      passwd="123"
#      un=input("请输入用户名")
#      ps=input("请输入密码")
#      if un==username and ps==passwd:
#          print("登录成功")
#          break
#      elif un!=username or ps!=passwd:
#          print("用户名或密码错误")
#          continue
# 4.冒泡排序给定一个无序列表list[39,19,11,109,5,6]对列表内容进行排序
# lst=[39,19,11,108,5,6]
# for i in range(len(lst)-1):
#     for j in range(len(lst)-1-i):
#         if lst[j]>lst[j+1]:
#             temp=lst[j]
#             lst[j]=lst[j+1]
#             lst[j+1]=temp
# print(lst)
# 下面是一个3*3的矩阵
# 3，8，9
# 6，11，2
# 7，18，5
# 实际上是一个二维列表
# [[3，8，9], [6，11，2], [7，18，5]]
# 通过键盘输入需要构造的矩阵维度，比如3*3, 2*2，
# 并根据维度接收对应数量的数，构成矩阵(二维列表)
#"如果我们要建立一个矩阵需要循环输入每行每列的值我们打算建立一个三行三列的矩阵")
# list0=[]
# for i in range(0,3):
#     list1=[]
#     for j in range(0,3):
#         list_num=int(input("请输入第%d行,第%d列的值" % (i + 1, j + 1)))
#         list1.append(list_num)
#     list0.append(list1)
#     print(list1)
# print("创建的三行三列的矩阵为"+str(list0))
#附加题求矩阵两条对角线的和
# list0=[[3,8,9], [6,11,2], [7,18,5]]
# for i in range(3):
#     for j in range(3):
#         if i==j:
