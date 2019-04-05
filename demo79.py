#爬虫框架scrapy

#创建tutorial爬虫项目：
#1：在C:\Users\admin\PycharmProjects文件夹下shift+鼠标右击选择‘在此处打开powershell窗口’，出现windows powershell窗口
#2：windows powershell窗口地址栏输入：scrapy startproject tutorial   即在此地址下创建tutorial项目文件夹
#创建爬虫爬取文件spider下的spider的py文件
#3：windows powershell窗口地址栏输入：cd tutorial
#4：windows powershell窗口地址栏输入：dir        会显示tutorial文件夹下路径文件名
#5：windows powershell窗口地址栏输入：scrapy genspider quotes quotes.toscape.com     quotes:爬虫文件名  quotes.toscape.com：网站域名
#项目建好了C:\Users\admin\PycharmProjects\tutorial
#爬虫文件也建好了，就可以开始写爬取规则获取内容了C:\Users\admin\PycharmProjects\tutorial\tutorial\spiders下的quotes.py文件
#执行哪个项目，就去哪个项目文件夹下shift+鼠标右击选择‘在此处打开powershell窗口’，出现windows powershell窗口输入命令行
#C:\Users\admin\PycharmProjects\tutorial\scrapydownloadertest  scrapydownloadertest这个项目放在了tutorial项目下，不冲突


#爬虫框架scrapy的selector模块取数据
# selector模块可调用xpath方法，正则，css选择器方法解析网页，提取数据
from scrapy import Selector

body = '<html><head><title>hello world!</title></head></html>'
selector = Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)