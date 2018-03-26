import os
from PIL import Image
# Loop over the images files in current directory
for f in listdir("."):
    if f.endswith(".png"):

        # makes image obejct of all files that ends with ".png"
        i = Image.open(f)

        # This will split the filename and filextn.Since we want to have same name but different extn.
        fn, fileExtn = os.path.splitext(f)

        # This will save the file with ".jpg" extn inside folder jpgs folder.
        i.save('jpgs/{}.jpg'.format(fn))