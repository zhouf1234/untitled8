import re
import requests

#这个帖子里面只有一张图片，。。。。。

#1. 爬取整个页面    爬贴吧
# request = requests.get('http://tieba.baidu.com/p/5970618267')
# with open('5970618267.txt',"wb+")as f:
#     f.write(request.content)

with open('5970618267.txt',"r",encoding='utf-8')as f:
    r=f.read()

#在整个页面中 爬取图片  利用正则匹配 需要的图片 src 地址
# d= re.sub('<div.*?>|</div>|<a.*?>|</a>|<li.*?>|</li>|<span.*?>|</span>|<ul.*?>|</ul>|<cc.*?>|</cc>','',r)
# s = re.findall('<img.*?src="(.*?)">',d,re.S)

pat = re.compile('src="(https://img.*?\.jpg)"')
s=re.findall(pat,r)
for i in s:
    print(i)
# print(s)


#图片命名,并不成功
# filname = re.search('sign=(.*?)\.jpg',i)
# filename=filname.group(1)
# print(str(filename))

# 保存到文件
req = requests.get(i)
with open('2.jpg',"wb+")as f:
    f.write(req.content)

