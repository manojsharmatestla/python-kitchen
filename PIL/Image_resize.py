import os
from PIL import Image
size_thumbnail = (250, 250)  # tuple defining the required size of image.
# Loop over the images files in current directory
for f in listdir("."):  
    if f.endswith(".png"):

        # makes image obejct of all files that ends with ".png"
        i = Image.open(f)

        # This will split the filename and filextn.
        fn, fileExtn = os.path.splitext(f)

        #create a thumbnail of size 250X250
        i.thumbnail(size_thumbnail) 
        i.save('thumbnail/{}_thumb{}'.format(fn,filextn))