from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)

locator = ("name", "tj_trmap")
text = "地图"
result = EC.text_to_be_present_in_element(locator, text)(driver)    #判断字段是否存在
print(result)