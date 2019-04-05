import tesserocr
from PIL import Image

#图像验证码识别，先装ocr，在下oct

#图片验证码识别
image = Image.open('code.jpg')
# res = tesserocr.image_to_text(image)    #识别的不准确
# print(res)

# res2 = tesserocr.file_to_text(image)用不了
# print(res2)

# image = image.convert('L')  #验证码转灰度，即颜色变灰，灰度处理
# image.show()


image = image.convert('L')
threshold = 129   #二值化阈值；二值化，去除验证码中多余的线条，要先灰度处理，如果识别有差异，调整阈值
table= []
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
# image.show()
res = tesserocr.image_to_text(image)    #如果识别错误，调整二值化阈值，code识别错误
print(res)
