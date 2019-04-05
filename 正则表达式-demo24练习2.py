import re
import requests


# 1. 爬取整个页面    爬贴吧
# request = requests.get('https://tieba.baidu.com/p/5969657105')
# with open('5969657105.txt',"wb+")as f:
#     f.write(request.content)

#读取爬取的文件
with open('5969657105.txt',"r",encoding='utf-8')as f:
    r=f.read()

#在整个页面中 爬取图片  利用正则匹配 需要的图片 src 地址
pat = re.compile('src="(https://img.*?\.jpg)"')
s=re.findall(pat,r)
# for i in s:
#     print(i)
# print(s)
for i in range(len(s)):
    print(s[i])



#比较悲剧，一次只能保存一张图片，并不简便
# req = requests.get(s[0])
# with open('4.jpg',"wb+")as f:
#     f.write(req.content)



