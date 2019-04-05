import requests
from lxml import etree

# 豆瓣影评，最受欢迎的影评，首页的影评人，标题，内容

#主页面爬取
header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('https://movie.douban.com/review/best/', headers=header)
request.encoding = 'utf-8'
d = request.text

#爬取网页内容，评论
html = etree.HTML(d)
# print(type(html))

# 10个影评内容,主页面用js写的展开，直接爬取恐怕有点问题，直接去分页吧
# 分页面网址分析  https://movie.douban.com/review/9593388/
bod = html.xpath("//div/@data-cid")
# print(bod)
for i in bod:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get('https://movie.douban.com/review/'+i, headers=header)
    request.encoding = 'utf-8'
    d2 = request.text

    html2 = etree.HTML(d2)  #初始化

    # 10个影评人id
    aothor2 = html2.xpath("//div[@class='main']//header[@class='main-hd']//a/span/text()")
    # print(aothor2)
    for a in aothor2:
        print(a)

    # 10个影评标题
    title2 =html2.xpath("//div[@class='article']//h1/span/text()")
    # print(title2)
    for i in title2:
        print(i)

    # 10个影评内容,
    bod2 = html2.xpath("//*[@id='link-report']/div[@class='review-content clearfix']//p//text()")
    # print(bod2)
    for d in bod2:
        print(d)

