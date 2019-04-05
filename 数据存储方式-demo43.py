import pymongo

#非关系型数据库mongdb存储
#mongodb可视化安装工具网址：https://robomongo.org/download,免费的robo3t那个
# http://api.mongodb.com/python/current/api/pymongo/collection.html可参考更多用法

#创建库和集合（表）
client = pymongo.MongoClient(host='localhost',port=27017) #创建mongodb对象
db = client.test  #指定数据库
collection = db.students   #指定集合（类似mysql的表名）


# 插入一条数据
student= {
    'id':'201801',
    'name':'bod',
    'age':20,
    'gender':'male'
}

# res = collection.insert(student)    #调用insert方法，插入数据,运行一次插入一次。。
# res = collection.insert_one(student)  #insert第二种官方推荐写法区分插入多条和一条数据
# print(res)      #显示：5c170f571fc1c842607a15b4表示已经插入数据,返回_id值

# 插入多条数据
student1= {
    'id':'201802',
    'name':'bob',
    'age':25,
    'gender':'male'
}
student2= {
    'id':'201803',
    'name':'mike',
    'age':22,
    'gender':'male'
}
# resu = collection.insert([student1,student2])    #调用insert方法，插入数据
# resu = collection.insert_many([student1,student2])    #insert第二种官方推荐写法区分插入多条和一条数据
# print(resu)     #显示：[ObjectId('5c1710001fc1c81d20a098c9'), ObjectId('5c1710001fc1c81d20a098ca')]


# 查询单个数据：第一种
resul = collection.find_one({'name':'mike'})
# print(resul)    #查询到就显示，未查询到就none
# print(type(resul))  #dict字典类型
# 第二种：


# 查询多个数据
# resul3 = collection.find()
resul3 = collection.find({'age':20})
# print(resul3)   #cursor类型，相当于生成器
# for i in resul3:
#     print(i)
# 查询多个数据2,查询条件小于'$lt'，大于'$gt'
resul4 = collection.find({'age':{'$lt':25}})
# print(resul4)
# for i in resul4:
#     print(i)


# 查询mongodb数据条数
count = collection.find().count()
# print(count)


# 排序
#内存过大时，不要用偏移量skip，limit，容易崩溃
xu = collection.find().sort('name',pymongo.ASCENDING).skip(70).limit(1)   #ASCENDING升序,skip():前面忽略多少个,limit():只取后面多少个
xu2 = collection.find().sort('age',pymongo.DESCENDING)   #DESCENDING降序
# print(xu)   #返回一个生成器
# print([x['name'] for x in xu])   #此处是按字母排序的name
# print(xu2)    #返回一个生成器
# for i in xu2:
#     print(i['age'])         #降序：年龄就按数字从大到小了

# 注意：在数据库数据量非常庞大的时候 如千万、亿级别 最好不要使用大的偏移量来查询数据 很可能会导致内存溢出
# 此时可以使用类似如下操作来查询

# from bson.objectid import ObjectId
# collection.find({'_id':{'$gt':ObjectId('_id值')}})


# 更新数据
condition = {'name':'mike'}
stu = collection.find_one(condition)
stu['age'] = 28
rstu = collection.update(condition,stu)           #三个rstu：三种更新方式都可
# rstu = collection.update(condition,{'$set':stu})
# rstu = collection.update_one(condition,{'$set':stu})    #one,更新一条，update_many:更新多条，官方推荐
# print(rstu)     #ture：更新成功了一条
# print(stu)      #更新成功，第一条的age改为了28


# 删除数据
# 第一种：此次删除了所有name= bob的24条数据
r = collection.remove({'name':'bob'})
# print(r)
# 第二种：删除一个或多个
r2 = collection.delete_one({'name':'bod'})  #一条，此次只擅长符合条件的一条
# r2 = collection.delete_many({'name':'bod'})  #多条，此次删除了所有符合条件的
# print(r2)   #DeleteResult类型
# print(r2.deleted_count)  #显示删除条数

# 查询所有的数据
res = collection.find()
for re in res:
    print(re)


