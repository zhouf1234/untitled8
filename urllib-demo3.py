import urllib.request   #请求模块

#timeout:服务器响应时间，超时就不响应，报错，无法爬取文件信息
res=urllib.request.urlopen('http://www.baidu.com',timeout=0.01)
print(res.read())