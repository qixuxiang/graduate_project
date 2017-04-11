from PIL import Image,ImageDraw
def binary1(im):
    pixels =im.load()
    for x in range(im.width):
        for y in range(im.height):
            pixels[x,y] = 255 if pixels[x,y]>127 else 0

def binary2(im):
    pixels =im.load()
    for x in range(im.width):
        for y in range(im.height):
            pixels[x,y] = 255 if pixels[x,y]>188 else 0

def binary3(im):
    pixels =im.load()
    for x in range(im.width):
        for y in range(im.height):
            pixels[x,y] = 255 if pixels[x,y]>210 else 0

def binary4(im):
    pixels =im.load()
    for x in range(im.width):
        for y in range(im.height):
            pixels[x,y] = 255 if pixels[x,y]>150 else 0

if __name__ == '__main__':
	img=Image.open('E:/47_n.png')
	binary1(img)
	img.save('E:/1b.png')
	binary2(img)
	img.save('E:/2b.png')
	binary3(img)
	img.save('E:/3b.png')
	binary4(img)
	img.save('E:/4b.png')
	
