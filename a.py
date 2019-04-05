import pymysql

# 连接入mysql数据库

# 创建数据库zhouju
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
# cursor.execute('CREATE DATABASE zhouju2 DEFAULT CHARACTER SET utf8')
# # 关闭数据库
# db.close()


# 无外键关联的表
# 在数据库开始建表，城市表zhouju_cityreg        ,都没有设置自增长。。。无语了
# 在数据库开始建表,首页省份表zhouju_regions
# 在数据库开始建表,院校类型表zhouju_scholl_types
# 在数据库开始建表,院校特征表zhouju_shool_features
# 在数据库开始建表,文章表zhouju_posts
# 在数据库开始建表，专业大分类表zhouju_major_big

# 有外键关联的表
# 在数据库开始建表，专业小分类表zhouju_majors  #外键关联了大分类表
#在数据库开始建表，院校信息表zhouju_schools   #外键关联了院校类型表，特征表，文章表，城市表，省表
# 在数据库开始建表，专业信息表zhouju_major_cates  #关联专业小分类表，院校信息表