import requests
import re
# 新浪新闻
#https://news.sina.com.cn/china/
# 正文右侧新闻标题
# 二级目录正文

# 分析页面
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('https://news.sina.com.cn/china/',headers=header)
request.encoding='utf-8'
s = request.text
# print(s)
print(type(s))

#正则取标题:第一次取到整个ul标签
pat=re.compile('<ul.*?class="news-2".*?>(.*?)</ul>',re.S)
new=re.findall(pat,s)
print(type(new))
for j in new:
    type(j)

# 第二次取到第一次取到的ul标签的li标签的所有a标签的内容，字符类型必须一致
patt1=re.compile('<li><a.*?>(.*?)</a></li>',re.S)
title=re.findall(patt1,j)
print(type(title))
for i in title:
    print(i)

# 保存,终于按序保存成文件了
# file=open("./files/sina新闻标题.txt","w+")
# for i in range (len(title)):
#     file.write(title[i]+"\n")
# file.close()


