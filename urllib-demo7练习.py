# 页码不出现负数
# 去贴吧帖子下级目录里面获取信息：即获取某一页中的某一个帖子的信息或获取贴吧帖子中的第n条到第n条帖子的信息

# 第三页
# https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=100
#第二页的某一个帖子，本次爬取的帖子地址
# https://tieba.baidu.com/p/5962687206

import urllib
import urllib.request
import urllib.parse

# isdigit()：所有字符都是数字
#def Begin()函数对象是为了使爬取某一整页信息时，输入起始页数不能为0或不是数字的输入判断，应该是要应用在demo7，作为升级
def Begin():
    beginPage = input('请输入开始页面(整数)：')
    while True:
        if beginPage.isdigit():# 如果字符串里面所有字符都是数字
            if int(beginPage) <= 0:
                beginPage =1
                break
            else:
                beginPage=int(beginPage)
                break
        else:
            print('输入错误！')
            beginPage = input('请重新输入：')
    print(beginPage)
    print(type(beginPage))

#百度贴吧爬虫接口 组合url地址
def tiebaSpider(url):
    """
    作用：负责处理 url 分配每一个url去发送请求
    :param url: 处理第一个url
    :return: null
    """
    filename = str(p) + "的.html"    #爬取的文件的命名
        #组合url 发送请求
    fullurl = url + "/p/" + str(p)     #爬取信息的地址，如：https://tieba.baidu.com/p/5962687206 即：url  +  /p/  +输入的要爬取的帖子地址p
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

#模拟main 函数：内置变量 __name__ 的值 如果是 "__main__" 说明再被当脚本用，
#               如果__name__值是模块名(文件名), 说明在被当模块用
if __name__ == "__main__":
    p=input('请输入要爬取的帖子id：')
    url = "http://tieba.baidu.com"
    tiebaSpider(url)