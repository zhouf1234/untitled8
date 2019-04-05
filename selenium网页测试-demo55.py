from selenium import webdriver

# 延时等待
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)     #延时等待10秒在跳转页面
# browser.get('http://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)


# 显式等待until()方法
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser,10)
input=wait.until(EC.presence_of_element_located((By.ID,'q')))   #等待10秒，节点出现
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))  #等待10秒，节点出现，调用until方法，按钮可点击
print(input,button)

# 更多等待条件，使用方法可参考官方文档
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
# http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions