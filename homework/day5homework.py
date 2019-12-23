# 1. 读取一个txt文件，文件内容为
# 姓名， 邮箱
# abc，123@163.com
# xyz，456@163.com
# 得到结果并写入新文件中：
# abc的邮箱为123@163.com
# xyz的邮箱为456@163.com
#(1)读取test文件中的内容
def read_write():
 with open("D:\\test.txt","r")as f:
  #(2)把读取的内容保存到列表datas里面
  datas=f.readlines()
  data=datas[1:]
 with open("D:\\abc.txt","w")as f1:
   for i in data:
     xx=i.replace('，','的邮箱为')
     f1.writelines(xx)
     f1.flush()
read_write()