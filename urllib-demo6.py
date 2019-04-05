import urllib.request   #请求模块
import urllib.parse
import random


keyeord='交通大学'

re=urllib.parse.quote(keyeord)  #将内容更改为URL编码格式:编码格式
# re=urllib.parse.unquote(keyeord)    #解码格式
print(re)
print()

word = {"wd":"交通大学"}
res = urllib.parse.urlencode(word)  #将内容更改为URL编码格式
print(res)

wor = {"wd":"lol"}
res = urllib.parse.urlencode(wor)  #将内容更改为URL编码格式
print(res)