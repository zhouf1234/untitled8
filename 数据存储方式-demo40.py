import csv

# 存储文本的方法csv：写入

# 一行一行传数据
# newline=''：不写的话，读取时行与行之间有空行
with open ('data.csv','w',newline='')as csvfile:
    writer = csv.writer(csvfile)    #初始化写入对象
    writer.writerow(['id','name','age'])  #传入每行数据
    writer.writerow(['1001','mike','20'])
    writer.writerow(['1002','anna','16'])
    writer.writerow(['1003', 'jordan', '21'])


# delimiter =' '：使保存的文件内容里用空格替换逗号
with open ('data1.csv','w')as csvfile:
    writer = csv.writer(csvfile,delimiter =' ')    #初始化写入对象
    writer.writerow(['id','name','age'])  #传入每行数据
    writer.writerow(['1001','mike','20'])
    writer.writerow(['1002','anna','16'])
    writer.writerow(['1003', 'jordan', '21'])


# 在一行传入多行数据，参数为二维列表
with open ('data2.csv','w')as csvfile:
    writer = csv.writer(csvfile)    #初始化写入对象
    writer.writerow(['id','name','age'])  #传入每行数据
    writer.writerow([['1001','mike','20'],['1002','anna','16'],['1003', 'jordan', '21']])  #传入多行数据


#字典方式传入
with open ('data3.csv','w')as csvfile:
    fieldname = ['id','name','age']  #定义字段
    writer = csv.DictWriter(csvfile,fieldnames=fieldname)#初始化字典写入对象
    writer.writeheader() #写入头信息
    writer.writerow({'id':'1001','name':'mike','age':'20'})
    writer.writerow({'id':'1002','name': 'bod', 'age': '21'})
    writer.writerow({'id': '1003', 'name': 'jordan', 'age': '22'})


# 输入中文，给open（）加入参数encoding=utf-8
with open ('data4.csv','w',encoding='utf-8')as csvfile:
    fieldname = ['id','name','age']  #定义字段
    writer = csv.DictWriter(csvfile,fieldnames=fieldname)#初始化字典写入对象
    writer.writerow({'id':'1001','name':'小米','age':18})