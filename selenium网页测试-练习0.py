from selenium import webdriver


# 此次获取豆瓣的读书，推理类的书名，作者，内容简介，第一页吧
# 分析：第一页https://book.douban.com/tag/推理?start=0&type=T
# 分析：第二页https://book.douban.com/tag/推理?start=20&type=T

page = 1        #第一页
start = (page-1)*20
tit = '推理'      #推理类
url = 'https://book.douban.com/tag/'
url = url+tit+'?start='+str(start)+'&type=T'     #url拼接
# print(url)

#此次获得推理页面主页面所有第一页的书名20个，作者和内容简介在分页面，尝试一下
douban = webdriver.Chrome()
douban.get(url)
books = douban.find_elements_by_css_selector('.subject-list li h2 a')
# print(books)    #获取的是一个列表
for i in books:
    print(i.get_attribute('title'))  #获得推理页面所有第一页的书名20个，作者和内容简介在分页面，尝试一下
douban.close()

# 尝试获取分页面连接吧,有20个分页面，太费时间，换个网址吧，selenium似乎也不是这么用法
# douban2 = webdriver.Chrome()
# douban2.get(url)
# url2 = douban2.find_elements_by_css_selector('.pic a')
# # print(url2)
# for u in url2:
#     # print(u.get_attribute('href'))
#     douban_book = webdriver.Chrome()
#     douban_book.get(u.get_attribute('href'))
#     douban_book.find_element_by_css_selector('#wrapper h1 span')
#     print(douban_book)      #太费电脑运行时间了。。。换个网址吧
#     douban_book.close()