import requests
import re
import urllib.parse
import urllib.request
import json
# 今日头条，搜索街拍，某一所有图片（此次第一页所有图片）

# 因为页面是可以不断用ajax动态刷新加载的，并不是按一页页标明，直接f12键，network键，disable勾选，XHR，刷新，下拉，可查看每页Headers 的Request URL和Previwe(含当前页面所有信息的)
# https://www.toutiao.com/search/?keyword=街拍

#实际第一页的Request URL，下拉页面分析，找第一页和第二页，第三页的差异
# https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis
page = 1               #选择第一页
offset=(page-1) *20
kw = '街拍'              #搜索关键字是街拍
keyword = urllib.parse.urlencode({"keyword":kw})
url = 'https://www.toutiao.com/search_content/?offset='
url = url+ str(offset)+'&format=json&'+str(keyword)+'&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis'
# print(url)          #url拼接

# 爬取内容
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get(url,headers=header)
c = request.text
# c = json.loads(request.text)
# print(c)
# print(type(c))

# 爬取跳转的图片的分url,然后拼接
pat=re.compile('"url":\s+"//.*?list/(.*?)"',re.S)
title=re.findall(pat,c)
# print(len(title))
# for i in title:
#     i2 = 'http://p99.pstatp.com/large/'+i
#     print(i2)
# for j in range(len(title)):         #拼接图片url，并保存到本地，此次已经运行
#     print("s[%d]=%s" % (j, 'http://p99.pstatp.com/large/'+title[j]))
    # urllib.request.urlretrieve('http://p99.pstatp.com/large/'+title[j], '%s.jpg' % j)


# 第二种尝试
# #爬取标题,都是Unicode码，json的方法可以使获得的页面的unicode码变成中文，但是也都变成字典类型了，无法直接正则查询。。
# patt=re.compile('"title":\s"(.*?)"',re.S)
# titles=re.findall(patt,c)
# print(titles)
# # for i in titles:
# #     # 终于找到了靠谱的，可以了，成功转码
# #     # print(i.encode('latin-1').decode('unicode_escape'))
# for i in range(len(titles)):
#     print("%d:%s" % (i, titles[i].encode('latin-1').decode('unicode_escape')))












