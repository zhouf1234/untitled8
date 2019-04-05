import requests
from lxml import etree

#xpath改写
# 新浪新闻
#https://news.sina.com.cn/china/
# 正文右侧新闻标题
# 二级目录正文

#爬取主页面文件
def loadPage(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    s = request.text
    return s

#写正则找文件地址
def urll(s):
    # 取到所有网页的连接
    html = etree.HTML(s)
    res = html.xpath("//ul[@class='news-2']//li[position()<11]/a/@href")
    # print(res)
    for i in res:
        # print(i)
        loadPage2(i)

#写正则找分文件内容
def loadPage2(i):
    #爬取网页连接的内容，正文
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    reques = requests.get(i, headers=header)
    reques.encoding = 'utf-8'
    s2 = reques.text

    # 取到所有网页的正文
    htm = etree.HTML(s2)
    re = htm.xpath("//div[@class='article']//p/text()")
    # print(re)
    for j in re:
        # print(j)
        write_to_file(j)

# 保存文件，只保存在一个文件里面，如何保存成10个文件呢
def write_to_file(j):
    #不能用w+的方式，因为是一行一行进去的
    with open('xpath练习4.txt','a',encoding='utf-8') as f:
        f.write(j+'\n')


#模拟main 函数，脚本就运行
if __name__=="__main__":
    url='https://news.sina.com.cn/china/'
    s=loadPage(url)
    urll(s)