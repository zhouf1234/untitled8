#phantomjs的方法

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)      #请求网页连接，虽然报错，但是也成功获取了