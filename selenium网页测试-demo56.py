import time
from selenium import webdriver

# 网页前进，后退
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
browser.get('https://www.baidu.com')
browser.get('https://www.python.org')
browser.back()  #后退到上一步即，回到了百度网页面了
time.sleep(2)
browser.forward()   #前进到下一页面，又回到python网页面了
browser.close()