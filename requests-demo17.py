import requests
#相当于打开两次网页
# 请求网址，设置cookies

#定义一个变量，接收session对象
s=requests.session()
#发送请求 设置cookie 'number','123456'
#verify = False:忽略网站ssl证书验证
s.get('http://httpbin.org/cookies/set/number/123456',verify = False)
#获取当前cookie
req = s.get('http://httpbin.org/cookies')
#成功获取
print(req.text)