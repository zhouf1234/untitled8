# 第一页，每页五十条信息
# https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0
# https://tieba.baidu.com/f?kw=lol
# 第二页
# https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=50
# 第三页
# https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=100

import urllib
import urllib.request
import urllib.parse

#百度贴吧爬虫接口 组合url地址 起始页和终止页
def tiebaSpider(url,beginPage,endPage):
    """
    作用：负责处理 url 分配每一个url去发送请求
    :param url: 处理第一个url
    :param beginPage: 爬虫起始页
    :param endPage: 爬虫终止页
    :return: null
    """
    for Page in range(beginPage,endPage+1):
        pn = (Page-1)*50
        filename = "第" + str(Page) + "页.html"
        #组合url 发送请求
        fullurl = url + "&pn=" + str(pn)        ## https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=50：url+
        # print(fullurl)
        # 调用loadPage（）函数发送请求获取HTML页面
        html = loadPage(fullurl,filename)
        # 调用writePage()函数 将服务器响应文件保存到本地磁盘
        writeFile(html,filename)

def loadPage(url,filename):
    """
    作用：根据url发送请求 获取服务器响应数据
    :param url: 请求地址
    :param filename: 文件名
    :return:服务器响应文件
    """
    print("正在下载" + filename)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    return response.read()

def writeFile(html,filename):
    """
    作用：保存服务器文件到本地磁盘
    :param html: 服务器文件
    :param filename:本地磁盘文件名
    :return:null
    """
    print("正在存储" + filename)
    with open(filename,"wb+") as f:
        f.write(html)
    print("-"*20)

#模拟main 函数
if __name__ == "__main__":
    kw = input("请输入要爬取的贴吧名")
    #输入起始页和终止页 str转化为int类型
    beginPage = int(input("请输入爬取的起始页"))
    endPage = int(input("请输入爬取的终止页"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw":kw})     #将内容更改为URL编码格式,示例见demo6，此次lol改为url编码格式后依然时lol

    url = url + key         #组合后的url示例 http://tieba.baidu.com/f?kw=lol
    tiebaSpider(url,beginPage,endPage)
