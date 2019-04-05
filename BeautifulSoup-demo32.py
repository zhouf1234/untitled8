from bs4 import BeautifulSoup

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
<li class="element">Foo<p></li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))  #查找class为这两个的节点
print()
print(soup.select('ul li'))     #查找ul中的li节点
print()
print(soup.select('#list-2 .element'))  #查找id为list-2且class为element的节点
print()

for ul in soup.select('ul'):
    print(ul['id'])          #查找ul节点中id的属性：显示list-1  list-2
    # print(ul.attrs['id'])     #两个print()返回结果一样
print()

for li in soup.select('ul'):
    print('get text:',li.get_text())    #查找ul节点中li节点的文本内容
    # print('String:',li.string)        #莫名为none