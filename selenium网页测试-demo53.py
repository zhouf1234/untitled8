from selenium import webdriver

# 获取节点信息：
# get_attribute()方法获取节点属性
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# logo = browser.find_element_by_id('zh-top-link-logo')     #获取id='zh-top-link-logo'的节点
# print(logo)     #webelement类型
# print(logo.get_attribute('class'))  #显示class节点属性值：zu-top-link-logo
#
#
# # text获取文本值
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)    #webelement类型
# print(input.text)   #显示：提问

#获取节点的ID，位置，标签名，大小
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)         #id值
print(input.location)   #位置，x，y轴
print(input.tag_name)   #所在标签名
print(input.size)       #大小：宽，高