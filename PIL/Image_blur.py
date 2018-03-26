import os
from PIL import Image
imageShow = Image.open('test.png')
imageShow.filter(ImageFilter.GaussianBlur(15)).save('test_blur.png')