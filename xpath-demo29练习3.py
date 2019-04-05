import requests
from lxml import etree

#xpath改写
# 新浪新闻
#https://news.sina.com.cn/china/
# 正文右侧新闻标题

# 分析页面
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('https://news.sina.com.cn/china/',headers=header)
request.encoding='utf-8'
s = request.text
# print(s)

html = etree.HTML(s)
# print(type(html))
res = html.xpath("//ul[@class='news-2']//li[position()<11]/a/text()")
# print(res)
for i in res:
    print(i)