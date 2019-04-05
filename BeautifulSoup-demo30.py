from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)    #Hello
print()



html='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their name were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
sou = BeautifulSoup(html,'lxml')    #初始化
print(sou.prettify())               #把要解析的字符串以标准缩进形式输出
print(sou.title.string)             #输出title节点中的文本内容:显示The Dormouse's story
print()
print(type(sou.prettify()))         #str数据类型
print(type(sou.title.string))       #<class 'bs4.element.NavigableString'>数据类型
print()

print(sou.title)                #获取title节点:显示<title>The Dormouse's story</title>
print(type(sou.title))          #<class 'bs4.element.Tag'>类型
print()

print(sou.head)             #获取head节点：显示<head><title>The Dormouse's story</title></head>
print(sou.p)                #获取p节点，结果只有一个<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
print()

print(sou.title.name)       #获取节点名称：显示title
print(sou.p.attrs)          #获取p节点所有属性，返回结果是字典形式{'class': ['title'], 'name': 'dormouse'}，只拿到第一个p节点的
print(sou.p.attrs['name'])  #显示：dormouse
print(sou.p['name'])        #显示：dormouse
print(sou.p['class'])       #显示一个列表：['title']
print(sou.p.string)         #输出p节点文本内容，就一个
print()

print(sou.head.title)       #获取head节点下的title节点
print(type(sou.head.title)) #<class 'bs4.element.Tag'>类型
print()

print(sou.p.contents)       #返回p标签的直接子节点的列表，显示[<b>The Dormouse's story</b>]
print(sou.p.children)       #返回结果是迭代器
for i,child in enumerate(sou.p.children):   #遍历迭代器，得到结果
    print(i,child)
print()

print(sou.p.descendants)    #返回结果是生成器
for i,child in enumerate(sou.p.descendants):   #遍历生成器，得到结果
    print(i,child)          #0 <b>The Dormouse's story</b>  1 The Dormouse's story
print()

print(sou.p.parent)        #返回父节点<body>所有内容了
print()
print(sou.p.parents)        #返回生成器
print()
print(list(enumerate(sou.p.parents)))   #列表输出索引和内容,此处三个列表。。。
print()

print('next:',sou.a.next_sibling)    #获取节点的下一个兄弟元素
print('pre:',sou.a.previous_sibling)       #获取节点的上一个兄弟元素
print('next',list(enumerate(sou.a.next_sibling)))      #获取后面的兄弟节点
print('pre',list(enumerate(sou.a.previous_sibling)))  #获取前面的兄弟节点
print()

print(type(sou.a.next_sibling))     #<class 'bs4.element.NavigableString'>
print(sou.a.next_sibling.string)        #,
print(sou.a.previous_sibling.string)    #上一个兄弟元素的文本内容：显示Once upon a time there were three little sisters; and their name were
print(type(sou.a.parents))              #<class 'generator'>生成器类型
print(list(sou.a.parents)[0])           #父节点索引值为0的节点和内容
print(list(sou.a.parents)[0].attrs['class'])    #父节点p的class属性值['story']
