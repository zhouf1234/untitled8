from selenium import webdriver

# 获取cookie：get_cookies()
# 添加cookie：add_cookie()
# 删除cookie：delete_all_cookies()

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())    #显示一个列表
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germery'})
print(browser.get_cookies())    #显示一个列表，添加的cookie在最后面
browser.delete_all_cookies()
print(browser.get_cookies())    #显示空列表