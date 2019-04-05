from selenium import webdriver
import time

# 操作网页选项卡，即浏览器开启多个网页页面；切换，添加
# 此次的显示为：先打开淘宝网页，再开百度网页共两个网页选项卡，然后淘宝网页切换为python网页
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
browser.execute_script('window.open()')
print(browser.window_handles)   #window_handles：返回当前会话中所有窗口的句柄 ，使鼠标可以操作淘宝网页面，使之最后跳转到python页面
browser.switch_to_window(browser.window_handles[1])   #[1]此句使重新打开一个新窗口，如果写[-1],就只会有一个窗口
browser.get('https://www.baidu.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.python.org')