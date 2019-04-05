import re
import urllib.request

#百度贴吧爬虫接口 组合url地址 ，爬取贴吧某一个帖子某一页所有图片文件，此帖子目前只有一页

#爬取贴吧帖子主页面文件
def loadPage(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    r=str(response.read())
    return r

#写正则找图片,命名并保存
def urll(r):
    pat = re.compile('src="(https://img.*?\.jpg)"')
    s = pat.findall(r)
    print(s)
    for i in range(len(s)):
        print("s[%d]=%s" % (i, s[i]))
        #urllib.request.urlretrieve用于下载链接URL的内容到本地filepath里面
        urllib.request.urlretrieve(s[i], '%s.jpg' % i)

#模拟main 函数，脚本就运行
if __name__=="__main__":
    url="https://tieba.baidu.com/p/5969657105"
    r=loadPage(url)
    urll(r)




