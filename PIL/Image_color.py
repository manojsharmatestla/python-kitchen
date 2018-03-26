import os
from PIL import Image,ImageFilter #Import ImageFilter also
imageShow = Image.open('test.png')
imageShow.convert(mode='L').save('test_blackWhite.png')