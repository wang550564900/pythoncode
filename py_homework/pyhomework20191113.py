# 1有如下值集合 [11,22,33,44,55,66,77,88,99,90]
# ，将所有大于 66 的值保存至字典的第一个 key 中，
# 将小于 66 的值保存至第二个 key 的值中。
# # 即： {'k1': 大于 66 的所有值,'k2': 小于 66 的所有值}
# lst=[11,22,33,44,55,66,77,88,99,90]
# lst1=[]
# lst2=[]
# dt={}
# for i in range(len(lst)):
#     if lst[i] > 66:
#       lst1.append(lst[i])
#     elif lst[i]<66:
#       lst2.append(lst[i])
# 为键为'k1'字典赋值，值为一个列表lst1
# dt['k1']=lst1
# dt['k2']=lst2
# print(dt)
# 2自定义一个list，每暂停一秒输出一个元素(使用 time 模块的 sleep() 函数)
# import time
# lst=[1,6,8,46,65,65,4,5]
# for i in range(len(lst)):
#     time.sleep(1)
#     print(lst[i])
# 3.有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
lst1= []
count=0
lst = ['1', '2', '3', '4']
for i in range(len(lst)):
    bw = lst[i]
    for j in range(len(lst)):
        sw = lst[j]
        for n in range(len(lst)):
            gw = lst[n]
            if bw != sw and sw != gw and bw!=gw:
                num1= bw + sw + gw
                count=count+1
                lst1.append(num1)
print(lst1)
print(count)
