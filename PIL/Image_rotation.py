import os
from PIL import Image
imageShow = Image.open('test.png')

# rotate image by 90 degress and save
imageShow.rotate(90).save('test_rotate.png') 