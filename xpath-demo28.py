from lxml import etree


text='''
<li class="li li-first"><a href="link2.html">first item</a></li>
'''
tes = etree.HTML(text)
#第一种方法：某个节点某个属性有多个值，需要获取文本内容
te = tes.xpath("//li[@class='li li-first']/a/text()")
print(te)
#第二种方法contains比较简洁
#contains：第一个参数是属性名称，第二个是属性值，和第一种方法的区别
t = tes.xpath("//li[contains(@class,'li')]/a/text()")
print(t)
print()



uext='''
<li class="li li-first" name="item"><a href="link2.html">first item</a></li>
'''
ues = etree.HTML(uext)
#第一种方法：某个节点多个属性有多个值，需要获取文本内容
ue = ues.xpath("//li[@class='li li-first']/a/text()")
print(ue)
#第二种方法
u = ues.xpath("//li[contains(@class,'li') and @name='item']/a/text()")
print(u)
#第三种方法
u2 = ues.xpath("//li[contains(@class,'li') or @name='item']/a/text()")
print(u2)