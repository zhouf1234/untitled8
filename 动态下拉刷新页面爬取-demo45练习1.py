import requests
import re

# 某一新浪微博主内容，转发数量，留言数量，点赞数量,未完成。微博内容有点问题。建议用demo45练习2

page = 1   #选择页数：第几页
uid = 1669879400  #选择微博主网页的uid：同https://m.weibo.cn/profile/1669879400的1669879400
nurl = '/api/container/getIndex?containerid=230413'
nurl = nurl+str(uid)+'_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page='+str(page)
# print('https://m.weibo.cn'+nurl)    #连接拼接

# 爬取页面,获取的中文是unicode码
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('https://m.weibo.cn'+nurl,headers=header)
c = request.text
# print(c)

# 微博主微博点赞数
# patt=re.compile('"created_at".*?"attitudes_count":(\d+)',re.S)
# titles=re.findall(patt,c)
# print(len(titles))
#
# # # 微博主微博评论数
# pat=re.compile('"created_at".*?"comments_count":(\d+)',re.S)
# title=re.findall(pat,c)
# print(len(title))
#
# # # 微博主微博转发数
# pa=re.compile('"created_at".*?"reposts_count":(\d+)',re.S)
# titl=re.findall(pa,c)
# print(len(titl))

# 微博主微博内容,总共10条，只取到8条,有些没出来，有些和上一条黏在一起了，建议不用此方法取内容
p = re.sub('<a.*?>|<.*?a>|@','',c)
# print(p)
p2 = re.compile('"text":"(.*?)"',re.S)
tit = re.findall(p2,p)
print(len(tit))
for i in tit:
    print(i.encode('latin-1').decode('unicode_escape'))
