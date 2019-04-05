import requests
import json
import re

# Ajax分析和抓取方式，这其实也是JavaScript动态渲染页面的一种情形
# 下拉即刷新的微博用ajax动态刷新加载的，并不是按一页页标明

# 爬取某一新浪微博主某一页微博内容，转发数量，留言数量，点赞数量，此次的微博主是迪丽热巴，是第一页

page = 1   #选择页数：第几页
uid = 1669879400  #选择微博主网页的uid：同https://m.weibo.cn/profile/1669879400的1669879400，在首页点击微博主即跳转的https://m.weibo.cn
nurl = '/api/container/getIndex?containerid=230413'
nurl = nurl+str(uid)+'_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page='+str(page)
# print('https://m.weibo.cn'+nurl)    #连接拼接

# 爬取页面,获取的中文是unicode码
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('https://m.weibo.cn'+nurl,headers=header)
c = json.loads(request.text)    #json序列化，全部变成字典格式
# print(c)
# print(c.keys())   #查询所有键名
# print(c['data']['cards'])     #找到字典中中的字典

# 按字典键名找到需要的内容：全都找到了，当前页十条
for i in c['data']['cards']:
    if i['card_type'] == 9:
        print('转发数：%s' %(i['mblog']['reposts_count']))
        print('评论数：%s' % (i['mblog']['comments_count']))
        print('点赞数：%s' % (i['mblog']['attitudes_count']))
        # print(i['mblog']['text'])
        i2 = re.sub('<a.*?>|</a>|<span.*?>|</span>|<img.*?>','',i['mblog']['text'])
        print('微博内容：%s' %i2)
