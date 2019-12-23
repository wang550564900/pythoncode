# 1. 从键盘接收一个输入，输入成绩，当输入的成绩在60以下时，
# 打印不及格，60-79打印及格，80及以上打印优秀
# while True:
#     score=input("请输入你的成绩:")
#     score1=int(score)
#     if score1 >= 80:
#         print("您真是太优秀")
#     elif score1>60 and score1<79:
#         print("还凑乎吧")
#     else:
#         print("60分都上不了回家玩泥巴去吧再见")
#         break
# else:
#     print()
# 2.输入一个整数，如果此数为0，则输出”石头”,
# 如果此数为1，则输出”剪刀”,如果此数为2，
# 则输出”布”,如果为其它，则输出”错误”
# while True:
#     num=int(input("请输入你的数字"))
#     if num==0:
#         print("石头")
#     elif num==1:
#         print("剪刀")
#     elif num==2:
#         print("布")
#     else:
#         print("错误")
# 3. 输入一个int型的数据，判断这个数是否能被2整除，
# 如果能被2整除，那么输出“这个数是偶数”，
# 否则输出“这个数是奇数”。
# while True:
#     num=int(input("请输入int型的数据"))
#     if num%2==0:
#         print("这个数是偶数")
#     else:
#         print("这是个奇数")
# 4. 输入两个整数，放入到a与b变量中去，
# 如果a>=b就将a与b中的值进行交换，否则就不交换。
# 目的就是要让a中放的值总是小于或等于b中的数，输出。
# while True:
#      a=int(input("a="))
#      b=int(input("b="))
#      c=0
#      if a>b:
#         c=a
#         a=b
#         b=c
#         print("a的值是："+str(a) + ", b的值是:"+str(b))
#      else:
#        print(a, b)
# else:
#         print(a,b)
# 5. 输入三个int型的数据，放入到a,b,c三个变量中去，
# 使用条件结构与交换逻辑将这三个变量中的值从小到大排列。
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a<b :
#     if a>c:
#         print("abc从小大依次为:"+str(c)+","+str(a)+","+str(b))
#     elif a<c:
#           if c>b:
#            print("abc从小大依次为:" + str(a) + "," + str(b) + "," + str(c))
#           elif b>c:
#               print("abc从小大依次为:" + str(a) + "," + str(c) + "," + str(b))
# elif a>b:
#        if a<c:
#          print("abc从小大依次为:" + str(b) + "," + str(a) + "," + str(c))
#        elif a>c:
#            if b>c:
#                print("abc从小大依次为:" + str(c) + "," + str(b) + "," + str(a))
#            elif b<c:
#                print("abc从小大依次为:" + str(b) + "," + str(c) + "," + str(a))
#6. 输入一个三位整数，判断其是不是降序数如:531是降序数 百位>十位>个位
# while True:
#           num=int(input("请输入一个三位整数"))
#           a=num//100%10
#           b=num//10%10
#           c=num//1%10
#           if a>b>c:
#            print("这是一个降序数")
#           else:
#               print("这是不是一个降序数")
# 7. 输入一个年份，判是闰年还是平年
# （能整除4、400，不能整除100）
# 1000不是闰年 2000 是一个闰年
# while True:
#     year=int(input("请输入年份"))
#     if year%4==0 & year%400==0&year%100!=0 or year==2000:
#      print("今年是闰年")
#     else:
#      print("今年不是闰年")
#8.
# while True:
#       print("如果你不是来上厕所的那么就欢迎您光临中国银行")
#       passwd=input("请输入您的密码：")
#       passwd1=int(passwd)
#       if passwd1==123456:
#        print("恭喜输入正确请输入第二道密码：")
#        passwd2=int(input())
#        if passwd2==654321:
#         print("恭喜输入两次密码正确这是您的1千万请慢走")
#        else:
#         print("大胆毛贼你第一次输入的密码是蒙的吧来人啦有抢银行的")
#       else:
#        print("你确定你不是来抢银行的？大胆毛贼")
# 9 纸张可以无限次对折，纸张厚度为0.07毫米。
# # 问多少次对折至少可以超过8848米？
# time=0
# h=8848*1000*100
# w=7
# while True:
#         w=w*2
#         print(w)
#         time=time+1
#         print(time)
#         if w>=h:
#          print(str(time) + "次对折至少可以超过8848米")
#          break