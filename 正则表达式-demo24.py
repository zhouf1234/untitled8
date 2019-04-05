import re

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

#match:从第一个字符串开始匹配第一个满足正则表达式的字符串，要求字符串一开始就要跟正则表达式匹配
#serch： 查找到第一个满足正则表达式的字符串 ，字符串中有地方跟正则表达式匹配就可以
#group的1是指第一个模式单元，正则加（）即为一个模式单元
res = re .search('\<\w\s\w{4}\=\"\/\d\.\w{2}\d\"\s\w{6}\=\"(\u9f50\u79e6)\">(\u5f80\u4e8b\u968f\u98ce)\<\/\w\>',html)
print(res)
print(res.group(1))
print(res.group(2))
print()


#搜索整个字符串，提取所有a节点的超链接，歌手，歌曲，第一种方法
r = re.findall('<a\shref="(.*?)"\ssinger="(.*?)">(.*?)</a>',html)
print(r)
for i in r:
    print(i)
print()

#搜索整个字符串，提取所有a节点的超链接，歌手，歌曲，第二种方法
r2 = re.findall('li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(r2)
# for j in r2:
#     print(r2[0],r2[1])
print()

#sub:替换,去掉一个字符串的所有数字
strs='34ibikalksajGDSOPX682j'
strs=re.sub('\d+','',strs)
print(strs)
print()

#获取所有li节点的歌名,第一种方法
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
for result in results:
    print(result[1])
print()

#sub方法获取所有li节点的歌名，第二种方法
s = re.sub('<a.*?>|</a>','',html)
fs = re.findall('<li.*?>(.*?)</li>',s,re.S)
# print(fs)
for k in fs:
    print(k.strip())    #去掉字符串两边的空格或换行符
print()

#目标使匹配齐秦 往事随风，发现其唯一的class=active
#re.S:使.匹配包括换行符在内的所有字符,写了之后。不用在正则李写空白符\s了
# .： 匹配任意字符除了 换行
#* ：前面的原子重复0次、1次到多次   {0,}
#.*?：阻止贪婪匹配
re = re.search('li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(re)
print(re.group(1))
print(re.group(2))
print()


