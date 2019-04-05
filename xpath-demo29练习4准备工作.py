import requests
from lxml import etree

#xpath改写
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
# print(type(s))

#取到所有网页的连接
html = etree.HTML(s)
res = html.xpath("//ul[@class='news-2']//li[position()<11]/a/@href")
# print(res)
# print(res[0])
# for i in res:
#     print(i)

# 网页连接的内容，正文
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
reques = requests.get(res[3],headers=header)
reques.encoding='utf-8'
s2 = reques.text

#取到所有网页的正文
htm= etree.HTML(s2)
re = htm.xpath("//div[@class='article']//p/text()")
# print(re)
for i in re:
    print(i)