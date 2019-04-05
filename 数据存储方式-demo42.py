import pymysql

# 关系型数据库存储
# 连接入mysql数据库

# 创建数据库
# # 声明一个mysql连接对象db
# db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306)
# #获取操作游标
# cursor = db.cursor()
# # mysql语句，获取当前mysql版本
# cursor.execute('SELECT VERSION()')
# # 获取第一条数据
# data = cursor.fetchone()
# print('database version:',data)
# # 创建名为spiders的数据库
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
# # 关闭数据库
# db.close()
#
# 建表students
# db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
# cursor = db.cursor()
# # 判断表是否存在，不存在就创建，否则报错
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()


# 给表中传入信息
# id = '20019'
# name = 'bobo'
# age = 24
# db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='spiders')
# cursor = db.cursor()
# # 上传数据的sql语句
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
# # sql = 'INSERT INTO students(id,name,age) values('+id+','+name+','+age+')'
# try:
#     cursor.execute(sql,(id,name,age))
#     db.commit() #执行数据插入
# except:
#     db.rollback()
# db.close()


# 给表中传入信息2,传入动态字典或元组,意思就是只需要传入一个元组或字典，下面的语句自动用，不用改写
# data = {
#     'id':'20020',
#     'name':'mike',
#     'age':24
# }
# print(data)
# db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='spiders')
# cursor = db.cursor()
# #
# table= 'students'   #定义表名
# keys = ','.join(data.keys())    #keys函数，取出键名，并用逗号拼接
# # print(keys)
# values = ','.join(['%s'] * len(data)) #获取data长度，逗号拼接
# # print(values)
# sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('successful')
#         db.commit() #执行数据插入
# except:
#     print('failed')
#     db.rollback()
# db.close()


# 更新数据,其实时根据id来更新的，name和age可以更改
# ON DUPLICATE KEY UPDATE 此条语句前后都是空格
# data = {
#     'id':'20020',
#     'name':'like sun',
#     'age':36
# }
# print(data)
# db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='spiders')
# cursor = db.cursor()
# #
# table= 'students'   #定义表名
# keys = ','.join(data.keys())    #keys函数，取出键名(id..)，并用逗号拼接
# # print(keys)
# values = ','.join(['%s'] * len(data)) #获取data长度，逗号拼接
# # print(values)
# sql='INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table,keys=keys,values=values)
# update = ','.join(['{key}=%s'.format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql,tuple(data.values())*2):  #execute函数传入第二个参数，元组参数
#         print('successful')
#         db.commit() #执行数据插入
# except:
#     print('failed')
#     db.rollback()  #停止
# db.close()
# print(sql)
# print(update)

# 删除数据
# db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='spiders')
# cursor = db.cursor()
# table= 'students'   #定义表名
# condition = 'age<25'  #删除条件
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
# try:
#     if cursor.execute(sql):
#         print('successful')
#         db.commit() #执行数据插入
# except:
#     print('failed')
#     db.rollback()  #停止


# 查询数据
# db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='spiders')
# cursor = db.cursor()
# table= 'students'   #定义表名
# sql= 'SELECT * FROM {table}'.format(table=table)
# try:
#     cursor.execute(sql)
#     print('count:',cursor.rowcount) #获取查询结果条数
#
#     # one = cursor.fetchone()     #获取第一条数据，返回元组形式
#     # print('one:',one)
#
#     res = cursor.fetchall()   #获取结果的所有数据，如果写了上方的获取第一条数据，则指针下移，此处取到的会少一条数据
#     print('res:',res)
#     print(type(res))    #二维元组
#     for row in res:
#         print(row)      #遍历输出
# except:
#     print('failed')
# print()

# 查询数据2：上一种查询的方法，数据量大时，容易耗费内存
db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='spiders')
cursor = db.cursor()
table= 'students'   #定义表名
sql = 'SELECT * FROM {table} WHERE age>=20 '.format(table=table)
try:
    cursor.execute(sql)
    print('count:',cursor.rowcount) #获取查询结果条数
    row = cursor.fetchone()
    while row:              #每循环一次，指针偏移一条数据，简单高效
        print('row:',row)
        row = cursor.fetchone()
except:
    print('failed')
