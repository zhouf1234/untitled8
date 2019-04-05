import urllib.request   #请求模块

import urllib.parse     #分析模块

data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf_8')
res=urllib.request.urlopen('http://www.baidu.com/post',data=data)
print(res.read())