from bs4 import BeautifulSoup
import re

html='''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.find_all(name='ul'))     #查询所有ul节点
print(type(soup.find_all(name='ul')[0]))  #<class 'bs4.element.Tag'>类型
print()

#使用find_all查找所有ul中的li节点和li节点文本内容，find_all结果为列表
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))    #查找所有ul中的li节点
    for li in ul.find_all(name='li'):
        print(li.string)    #输出所有ul下li节点文本内容
print()

#使用attrs查找属性,'id'为'list-1'的节点
print(soup.find_all(attrs={'id':'list-1'}))     #结果为列表
print(soup.find_all(attrs={'name':'elements'})) #结果为列表
print()

#直接find_all查找id'为'list-1'的节点
print(soup.find_all(id='list-1'))   #返回'id'为'list-1'的节点
print(soup.find_all(class_='list'))
print(soup.find_all(class_='element'))  #返回'class'为'element'的节点
print()

#返回正则表达式匹配的节点文件组成的列表
print(soup.find_all(text=re.compile('Fo')))
print()

#find查找,和find_all用法不同的是，结果不再是列表形式，只有第一个匹配元素
print(soup.find(name='ul'))     #查询到第一个ul节点
print(soup.find(class_='list')) #返回'class'为'list'的第一个节点
print(soup.find(class_='element'))  #返回'class'为'element'的第一个节点
print(type(soup.find(name='ul')))   #<class 'bs4.element.Tag'>类型
print()

#find_parents()   返回所有祖先节点
# find_parent()     直接返回父节点
#find_next_siblings（） 返回后面所有兄弟节点
#  find_next_sibling()  返回后面第一个兄弟节点
#find_previous_siblings()   返回前面所有兄弟节点
#  find_previous_sibling()  返回前面第一个兄弟节点
#find_all_next()    返回节点后面所有符合条件的节点
# find_next()   返回第一个符合条件的节点
#find_all_previous()    返回节点后所有符合条件的节点
#    find_orevious()    返回第一个符合条件的节点

