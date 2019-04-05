import pytesseract
from PIL import Image

im = Image.open('code.jpg')

# 转化为灰度图像
im = im.convert('L')  # 转化为灰度图像
threshold = 129
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

im = im.point(table, '1')
print(pytesseract.image_to_string(im))  #调整二值化的threshold阈值


