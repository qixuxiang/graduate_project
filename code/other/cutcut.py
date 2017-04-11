from PIL import Image,ImageDraw
from pylab import *
im=Image.open('E:/47_n.png')
width,height = im.size
pix = im.load()
a = [0]*256
for w in range(width):
    for h in  range(height):
        p = pix[w,h]
        a[p] = a[p] + 1

s = max(a)
print(a,len(a),s) 	#长度256,a保存的分别是颜色范围0-255出现的次数
image = Image.new('RGB',(256,256),(255,255,255))  
draw = ImageDraw.Draw(image)  

for k in range(256):
    #print(k,a[k],a[k]*200/s)
    a[k] = a[k]*200/s		#映射范围0-200
    source = (k,255)   		#起点坐标y=255, x=[0,1,2....]
    target = (k,255-a[k])	#终点坐标y=255-a[x],a[x]的最大数值是200,x=[0,1,2....]
    draw.line([source, target], (100,100,100))
image.show()