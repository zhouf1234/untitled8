import requests
from lxml import etree


#爬取知乎网发现，今日热点的问题标题，回答者，回答。xpath的方法尝试
# https://www.zhihu.com/explore

#分析主页面
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
req = requests.get('https://www.zhihu.com/explore',headers=header)
c = req.text

# 初始化
html = etree.HTML(c)
# 获取热点标题
hea = html.xpath("//div[@class='explore-feed feed-item']//a[@class='question_link']/text()")
# print(hea)

# 获取回答者
aut = html.xpath("//div[@class='explore-feed feed-item']//div/@data-author-name")
# print(aut)

# 获取回答内容,取到的内容太多特殊字符了,只能分页面取了
write = html.xpath("//div[@class='explore-feed feed-item']//div/@data-entry-url")
# print(write)
for i in write:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    re = requests.get('https://www.zhihu.com'+i, headers=header)
    c2 = re.text

    htm = etree.HTML(c2)
    write2 = htm.xpath("//span[@class='RichText ztext CopyrightRichText-richText']/p/text()")
    # print(write2)

# 内容组合,也是个问题,内容加不进去。。考虑下爬取豆瓣影评的方法，直接分页面找所有的，就无需组合了
dictionary = list(zip(hea,aut))
print(dictionary)

