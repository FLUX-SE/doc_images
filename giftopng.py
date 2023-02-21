from PIL import Image, ImageDraw, ImageFont #dynamic import


import os
rootdir = './'
extensions = '.gif'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #ext = file.endswith(".gif") #os.path.splitext(file)[-1].lower()
        #print(ext)
        if file.endswith(".gif"): #ext in extensions:
            print (os.path.join(subdir, file))

            gif=os.path.join(subdir, file)
            img = Image.open(gif)
            img.save(gif.removesuffix('.gif')+".png",'png', optimize=True, quality=100)