import urllib.request
res=urllib.request.urlopen('http://www.baidu.com')
#和filder一起的时候就报错，关闭fiddler就可以了

# print(res.read())         #返回的响应文件内容，纯文本格式
# print(type(res))         #返回的是服务器响应类型：<class 'http.client.HTTPResponse'>
# print(res.status)           #返回的服务器响应的状态吗：200 ：表示我们请求成功
# print(res.getheaders())        #返回的请求头部的信息，设置的内容
print(res.getheader('Server'))  #返回服务器类型，根据网站有关的，每个网站都不一样


