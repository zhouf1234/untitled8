import re
content='''Hello 123 4567 World_This
is a Regex Demo'''

# content='Hello 123 4567 World_This' \
# #         'is a Regex Demo'

# 换行符也匹配到了,换行的时候此处自动产生了\换行符就不报错
#把换行符去掉就报错，添加了re.S就解决了
#re.S:使.匹配包括换行符在内的所有字符
res = re .match('^He.*?(\d+).*?Demo$',content,re.S)

print(res)
print(res.group(1))
print()


conten='(百度)/www.baidu.com'
resu = re .match('\(百度\)www\.baidu\.com',conten)
print(resu)
print()

conte='Auto Hello 123 4567 World_This is a Regex Demo'
resul=re.match('He.*?(\d+).*Demo$',conte)
print(resul)        #返回none，因为match是从第一位开始位置匹配的

cont='Auto Hello 123 4567 World_This is a Regex Demo'
resul2=re.search('He.*?(\d+).*Demo$',conte)
print(resul2)