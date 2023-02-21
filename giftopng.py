from PIL import Image, ImageDraw, ImageFont #dynamic import


import os
rootdir = './'
extensions = '.gif'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".gif"):
            print (os.path.join(subdir, file))
            gif=os.path.join(subdir, file)
            img = Image.open(gif)
            img.save(gif.removesuffix('.gif')+".png",'png', optimize=True, quality=100)