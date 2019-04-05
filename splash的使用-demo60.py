import requests
import json

# Splash是一个JavaScript渲染服务 是一个带有HTTP API的轻量级浏览器 同时对接了python的Twisted 和QT库，利用它可以实现对动态渲染页面的抓取
# 使用splash抓取内容
# 要先开启docker正常运行，并查看到本机ip地址，cmd命令行输入docker正常运行后，命令行再输入docker run -p 8050:8050 scrapinghub/splash  启动splash
# http://192.168.99.100:8050/    此次本机ip（192.168.99.100）进入splash地网址，通过谷歌浏览器


# splash接口获取javascript渲染的页面的html代码，接口地址既是splash运行地址加此接口名称
#此次获取的百度的html内容，render即splash地址网页的render绿键，html即获取的文件格式吧
url = 'http://192.168.99.100:8050/render.html?url=http://www.baidu.com'
response = requests.get(url)
# print(response.text)

# wait=5：延迟五秒后显示
#此次获取的淘宝的html内容
ur = 'http://192.168.99.100:8050/render.html?url=http://www.taobao.com&wait=5'
respons = requests.get(ur)
# print(respons.text)

# wait=5：延迟五秒后显示，width和height：设置图片宽和高
# 此次获取的是京东的首页图片png格式图片，也保存了,（也可以用jpeg的）
u = 'http://192.168.99.100:8050/render.png?url=http://www.jd.com&wait=5&width=1000&height=700'
respon = requests.get(u)
# with open('jd.png','wb')as f:
#     f.write(respon.content)


u2 = 'http://192.168.99.100:8050/render.json?url=http://www.jd.com&wait=5'
respo = requests.get(u2)
# 怎么读取或输出json呢。。。。。
