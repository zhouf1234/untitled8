#抓取网站图标，例如知乎的知图标
import requests

#https://www.zhihu.com/favicon.ico,网站图标网址，都加/favicon.ico

request = requests.get('http://www.baidu.com/favicon.ico')
# print(request.text)   #一堆乱码
# print(request.content) #一堆二进制形式的码,将它写入一个文件，可以读取

#'favicon.ico'：要保存的文件名，
with open('favicon.ico',"wb+")as f:
    f.write(request.content)