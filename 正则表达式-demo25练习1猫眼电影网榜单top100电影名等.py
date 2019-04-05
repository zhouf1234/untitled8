import re
import requests


#此次获取的是第一页的
#https://maoyan.com/board/4
#猫眼电影网的榜单top100：获取电影名，主演名，上映时间

# 1. 爬取整个页面:眼电影网的榜单top100
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('https://maoyan.com/board/4',headers=header)
m = request.text
# print(type(m))

# print(m)
#2:在整个页面中 爬取图片  利用正则匹配 需要的图片 src 地址
# <a title="肖申克的救赎" href="/films/1297" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a>
#<p class="star">主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿</p>
#<p class="releasetime">上映时间：1994-10-14(美国)</p>

# patt=re.compile('<a.*?title=.*?href=.*?data-act=.*?data-val=.*?>(.*?)</a>',re.S)
# patt=re.compile('<p.*?class="star">(.*?)</p>',re.S)----p标签和字符之间有空格，太多了，不用这个，用下面这个
# patt=re.compile('<p.*?class="star">\s+(.*?)\s+</p>',re.S)
# patt=re.compile('<p.*?class="releasetime">(.*?)</p>',re.S)

#此次获取的是第一页的
patt=re.compile('<a.*?title=.*?href=.*?data-act=.*?data-val=.*?>(.*?)</a>.*?<p.*?class="star">\s+(.*?)\s+</p>.*?<p.*?class="releasetime">(.*?)</p>',re.S)
titles=re.findall(patt,m)
print(titles)
for i in titles:
#     # print(type(i))    #类型是元组
#     # print(type(i[0])) #类型是字符串
#     print(i[1])
#     print(i[2])
    print(i)