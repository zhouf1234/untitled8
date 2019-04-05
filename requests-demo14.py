import requests

#获取cookie，并遍历解析
req = requests.get('http://www.baidu.com')
print(req.cookies)      #返回的是RequestCookieJar类型

for key,value in req.cookies.items():
    print(key + '=' + value)