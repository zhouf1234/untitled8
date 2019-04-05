from pyquery import PyQuery as pq

html = '''
<div class='warp'>
<div id='container'>
<ul class='list'>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''

doc = pq(html)
#移除active属性
# print(doc('.item-0.active').removeClass('active'))
# print()
#
# #添加active属性：不存在的就添加，存在就不增加
# print(doc('.item-1').addClass('actives'))
# print()

# attr()添加属性和属性值，第一个参数为属性名
print(doc('.item-0.active').attr('name','link'))
print()

#text()获取节点内纯文本，传入文本，直接修改了原来标签的文本内容
print(doc('.item-0.active').text('changed item'))    #<li class="item-0 active" name="link">changed item</li>
print()
#html()获取节点内部的html文本,传入html文本
print(doc('.item-0.active').html('<span>changed item</span>'))   #<li class="item-0 active" name="link"><span>changed item</span></li>
print()

#第一个li节点
print(doc('li:first-child'))
# 最后一个li节点
print(doc('li:last-child'))
#第二个节点
print(doc('li:nth-child(2)'))
#第三个li之后的li节点
li = doc('li:gt(2)')
print(li)
#偶数位置的li节点
li = doc('li:nth-child(2n)')
print(li)
#包含second文本的li节点
li = doc('li:contains(second)')
print(li)