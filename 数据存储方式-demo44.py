from redis import StrictRedis

# 非关系型数据库redis存储

# 连接数据库redis的db=0
redis = StrictRedis(host='localhost',port=6379,db=0)
# redis = StrictRedis(host='localhost',port=6379,db=0,password='foobared')
redis.set('name','bob')     #设置键值对
print(redis.get('name'))    #输出：b'bob'

from redis import StrictRedis,ConnectionPool

pool = ConnectionPool(host='localhost',port=6379,db=0)
# pool = ConnectionPool(host='localhost',port=6379,db=0,password='foobared')
redis = StrictRedis(connection_pool=pool)
print(redis.get('name'))    #输出：b'bob'


url = 'redis://@localhost:6379/0'
# url = 'redis://:foobared@localhost:6379/0'     #有设置密码时，本次没有设置密码。。。
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
print(redis.get('name'))        #输出：b'bob'

