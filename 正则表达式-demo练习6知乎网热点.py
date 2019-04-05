import re
import requests

#爬取知乎网发现，今日热点的问题标题，回答者，回答。解析方法不论，re正则表达式的方法
# https://www.zhihu.com/explore

#爬取主页面文件
def loadPage(url):
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    req = requests.get(url, headers=header)
    c = req.text
    return c

#写正则找文件地址
def urll(c):
    # 正则取标题
    patt = re.compile('<div.*?class="explore-feed.*?".*?>.*?<a.*?class="question_link".*?>(.*?)</a>', re.S)
    titles = re.findall(patt, c)
    # print(titles)
    # for i in titles:
    #     print('title:%s'%(i))
    return titles

def urlll(c):
    # 正则取回答者
    pat=re.compile('<div.*?data-author-name="(.*?)".*?>',re.S)
    title = re.findall(pat, c)
    # print(title)
    # for j in title:
    #     print('author:%s'%(j))
    return  title

def urllll(c):
    # 正则取回答内容
    patt = re.compile(
        '<div.*?class="zm-item-rich-text.*?">.*?<textarea hidden class="content">(.*?)</textarea>.*?</div>', re.S)
    tit = re.findall(patt, c)

    tit2 = []  #字符串组合成列表，因为先写替换正则有点问题，在遍历里写就没问题了，就需要重新组合成列表来最后进行组合输出
    for i in tit:
        i2 = re.sub(
            '&lt;|p&gt;|br&gt;|li&gt;|b&gt;|h2&gt;|/|figure&gt.*?figure&gt;|blockquote&gt;|a.*?&gt;|i&gt;|ul&gt;|hr&gt;',
            '', i)
        # print(i2)
        if i2 not in tit2:
            tit2.append(i2)     #将不需要的字符去除后重新组合进新列表
    return tit2


#分别组合了标题和作者和内容；考虑下面向对象方法。。。也考虑下其他解析方法吧，搞得有点复杂了
def zuhe(titles,title,tit2):
    dictionary = list(zip(titles, title,tit2))
    # print(dictionary)
    for i in dictionary:
        for j in i:
            print(j)

#模拟main 函数，脚本就运行
if __name__=="__main__":
    url='https://www.zhihu.com/explore'
    c=loadPage(url)
    # urll(c)
    # urlll(c)
    # urllll(c)
    titles = urll(c)
    title = urlll(c)
    tit2 = urllll(c)
    zuhe(titles,title,tit2)



