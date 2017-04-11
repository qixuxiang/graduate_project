import sys,os
from PIL import Image,ImageDraw
file_path='E:/'
img = Image.open(os.path.join(file_path,'scu.jpg' ))
print(img.size)
im=img.resize((940,625),Image.ANTIALIAS)
im.save(os.path.join(file_path,'scu1.jpg' ))
print(im.size)
