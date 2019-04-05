from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult') #切换到子frame
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('no logo!')               #子页面没有拿到，就输出了这个
browser.switch_to.parent_frame()    #切换到父frame
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)        #父frame，拿到了