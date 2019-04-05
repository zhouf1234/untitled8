import csv

# 存储文本的方法csv：读取
# 读取csv文件内容

# 'data.csv'写这个文件时有写newline=''，所有读取时没有空行，data2和data3没写，有空行
with open ('data.csv','r',encoding='utf-8')as csvfile:
    reader = csv.reader(csvfile)
    # print(reader)   #<_csv.reader object at 0x000001EAB8767A70>:一个csv对象
    for row in reader:
        print(row)
        # print(type(row))    #<class 'list'>类型
print()

with open ('data2.csv','r',encoding='utf-8')as csvfile:
    reader = csv.reader(csvfile)
    # print(reader)   #<_csv.reader object at 0x000001EAB8767A70>:一个csv对象
    for row in reader:
        print(row)
        # print(type(row))    #<class 'list'>类型
print()


with open ('data3.csv','r',encoding='utf-8')as csvfile:
    reader = csv.reader(csvfile)
    # print(reader)   #<_csv.reader object at 0x000001EAB8767A70>:一个csv对象
    for row in reader:
        print(row)
        # print(type(row))    #<class 'list'>类型
print()