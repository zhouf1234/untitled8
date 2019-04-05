from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

# 异常处理:防止异常中断，捕获异常
# 更多异常类：https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('time out')       #超时未连接到网页就输出此句
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('no element')     #未找到此节点就输出此句
finally:
    browser.close()