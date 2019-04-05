import selenium
from selenium import webdriver

# Selenium的使用
# selenium是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，例如 点击 下拉等操作，
# 同时还可以获取浏览器当前呈现的页面的源代码，做到可见既可爬。
# 对于一些js动态渲染的页面来说，此种爬取方式非常有效


# 谷歌浏览器的版本 71.0.3578.98（正式版本） （64 位）
# https://sites.google.com/a/chromium.org/chromedriver
# https://chromedriver.storage.googleapis.com/index.html
# 俩网站都可下载chromedriver（按谷歌版本号），chromedriver.exe放到python脚本文件里，C:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts


# 测试，弹出空白chrome谷歌浏览器页面，说明配置无误，版本兼容了；没有弹出则重新配置，闪退可能是版本不兼容
# browser = webdriver.Chrome()


#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()        #初始化

try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')    #获取id=kw的节点，即百度网输入框的节点
    input.send_keys('Python')   #相当于百度网输入框直接搜索‘python’
    input.send_keys(Keys.ENTER)     #相当于键盘的enter键，即：开始搜索
    wait = WebDriverWait(browser,10)    #等待时间：10秒，id=content_left的节点出现
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)          #请求网页连接
    print(browser.get_cookies())        #请求网页cookie
    print(browser.page_source)          #请求网页源代码，请求到的是搜索python后的网页源码
finally:
    browser.close()                 #关闭
