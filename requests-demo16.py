import requests

#相当于打开两次浏览器
#测试，请求网址，设置cookies
requests.get('http://httpbin.org/cookies/set/number/123456')
#获取cookies
req = requests.get('http://httpbin.org/cookies')
print(req.text)     #返回结果：{"cookies": {} }