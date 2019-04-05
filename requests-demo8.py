import requests

#第一种方法
# request = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(request.text)

#第二种方法
# data={
#     'name':'germey',
#     'age':22
# }
#
# request = requests.get('http://httpbin.org/get',params=data)
# print(request.text)


request = requests.get('http://httpbin.org/get')
print(type(request.text))   #str类型
print(request.json())       #json方法转化为字典型
print(type(request.json()))     #返回结果为字典型
