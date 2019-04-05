import urllib.request   #请求模块
import urllib.error
import socket

#timeout:服务器响应时间，超时就不响应，无法爬取文件信息
try:
    res=urllib.request.urlopen('http://www.baidu.com/get',timeout=0.01)
except urllib.error.URLError as e:
    isinstance(e.reason,socket.timeout)
    print('TIME OUT')