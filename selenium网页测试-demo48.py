from selenium import webdriver

from selenium.webdriver.common.keys import Keys

# 获取单个节点，此次是搜索框的标签节点
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')   #请求页面，传入连接url

# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_thrid = browser.find_element_by_xpath('//*[@id="q"]')

# print(input_first,input_second,input_thrid)     #这三种方法获取单个节点，获取的类型都是webelement，结果一致的

# # input_first.send_keys('外套')
# # input_first.send_keys(Keys.ENTER)
# # print(browser.page_source)      # #请求网页源代码,跳出了登陆框。。。登陆后可见搜索到的页面
# browser.close()

# 获取单个节点的另一种方法,find_element()传入俩参数：查找方式和值
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_four = browser.find_element(By.ID,'q')
print(input_four)
browser.close()


# 获取单个节点的方法,'q'的来源：淘宝网源码里搜索框的：<input id="q" name="q" aria-label="请输入搜索文字" accesskey="s" autofocus="autofocus" autocomplete="off" class="search-combobox-input" aria-haspopup="true" aria-combobox="list" role="combobox" x-webkit-grammar="builtin:translate" tabindex="0">
# find_element_by_id('q')
# find_element_by_name('q')
# find_element_by_css_selector('#q')
# find_element_by_xpath('//*[@id="q"]')
# find_element_by_link_text()   #通过链接文本查找元素。link_text：要查找的元素的文本。
# find_element_by_partial_link_text()   #通过元素链接文本的部分匹配查找元素
# find_element_by_tag_name()    #根据标签名称（a,div,h1...）查找元素
# find_element_by_class_name()