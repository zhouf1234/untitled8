import requests

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

data ={
    'name':'xiaomi',
    'age':23
}

req = requests.post('http://httpbin.org/post',data=data,headers=header)
print(req.text)         #响应内容对象
print(req.status_code)    #返回响应的状态码：200
print(req.cookies)          #返回cookie对象数据类型
print(req.url)          #返回url最终地址：http://httpbin.org/post
print(req.history)      #返回请求历史记录[]