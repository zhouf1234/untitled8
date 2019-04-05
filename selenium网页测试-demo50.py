from selenium import webdriver
import time

# 节点交互
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input=browser.find_element_by_id('q')       #获取网页搜索框id='q'
input.send_keys('iphone')   #搜索iphone
time.sleep(1)   #延迟一秒
input.clear()   #清空搜索记录iphone
input.send_keys('ipad')   #搜索ipad
# 淘宝网搜索键的：<button class="btn-search tb-bg" type="submit" data-spm-click="gostr=/tbindex;locaid=d13">搜索</button>
button = browser.find_element_by_class_name('btn-search')   #btn-search来自于此
#input.send_keys(Keys.ENTER)：点击按钮，这俩句任一都可
button.click()  #点击操作，没有写close，浏览器的页面就一直开着