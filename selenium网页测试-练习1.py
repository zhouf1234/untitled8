from selenium import webdriver
import time

# 豆瓣首页去到了豆瓣读书的页面,再去了豆瓣读书的推理书类页面，即二次跳转页面

# douban = webdriver.Chrome()
# douban.get('https://www.douban.com/')
# douban.find_element_by_class_name('lnk-book').click() #找到首页的读书页面的class=lnk-book的节点点击去往读书页面
# time.sleep(3)
# # 准备开始跳转到推理书类页面
# windows = douban.window_handles  #window_handles：返回当前会话中所有窗口的句柄 ，使之可以跳转到推理页面
# douban.switch_to.window(douban.window_handles[1])
# time.sleep(3)
# douban.find_element_by_xpath("//ul[@class='hot-tags-col5 s']//li[2]//ul[@class='clearfix']/li[3]/a").click()
# time.sleep(3)
# douban.close()


# 豆瓣读书页面点击去到推理书类页面，并取到推理书类页面第一页的书名20个,也可以取其他内容
# 一次跳转的页面爬取内容
douban = webdriver.Chrome()
douban.get('https://book.douban.com/')
# 从首页取到推理书类标签并点击跳转，li[2]:指书目分类li的第二大类推理类所在大类，li[3]：指推理书类所在ul下第三个li标签
douban.find_element_by_xpath("//ul[@class='hot-tags-col5 s']//li[2]//ul[@class='clearfix']/li[3]/a").click()
d = douban.current_window_handle    #//此行代码用来定位当前页面,使之可以取到推理书类页面标签内容
bookes = douban.find_elements_by_css_selector('.subject-list li h2 a')
# print(bookes)
for book in bookes:
    print(book.get_attribute('title'))  #获得推理页面第一页的所有书名20个
douban.close()



