import json

# 存储文本的方法json
#json都是双引号
str1= '''
[{
    "name":"bod",
    "gender":"male",
    "bir":"1992-03-10"
},{
    "name":"selina",
    "gender":"female",
    "bir":"1995-10-20"
}]
'''

print(type(str1))       #<class 'str'>
# print(str1)
data = json.loads(str1)   #显示列表中的字典格式，更易于理解，处理数据
print(data)
print(type(data))       #<class 'list'>
print()

print(data[0]['name'])
print(data[0].get('name'))
print()

#读取文本文件json的内容
with open('data.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    print(dat)
print()

da = [{
    "name":"bod",
    "gender":"male",
    "bir":"1992-03-10"
}]
# 将da的json文本以json序列化的方法写进
with open('data.json','w')as file:
    file.write(json.dumps(da,indent=2))     #indent:缩进字符两位


d = [{
    "name": "小牛",
    "gender": "男",
    "bir": "1992-03-10"
}]
with open('data.json','w')as file:
    file.write(json.dumps(d,indent=2,ensure_ascii=False))   #ensure_ascii=False:防止中文打开乱码