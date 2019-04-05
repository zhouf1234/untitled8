from selenium import webdriver

# 获取多个节点：find_elements()查找所有满足条件的节点，比单节点多了个s
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# 此次获取的是淘宝网右侧，<ul class="service-bd"...>...</ul>节点中的所有li节点，16个li节点，类型是webelement
lis = browser.find_elements_by_css_selector('.service-bd li')   #css选择器的方法
print(lis)
browser.close()

# 获取多个节点的方法
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_css_selector()
# find_elements_by_xpath()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_tag_name()
# find_elements_by_class_name()
