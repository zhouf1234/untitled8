import requests
import os

filepath = './banben/01'
if not os.path.exists(filepath):  # 如果文件夹不存在就创建,先建banben这个，在01分两步
    os.mkdir(filepath)

# request = requests.get('http://n5.1whour.com/newkuku/2014/201412/1220b/我叫坂本我最屌/Vol_1//0001IG9.jpg')
# # print(request.text)   #一堆乱码
# # print(request.content) #一堆二进制形式的码,将它写入一个文件，可以读取
#
# #要保存的文件名，
# with open('03.jpg',"wb+")as f:
#     f.write(request.content)