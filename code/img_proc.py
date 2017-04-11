'''
@Author qixuxiang
@Date 2016.03.05
ima_proc.py
图片预处理，包括调整大小、灰度化、二值化和去噪点
'''
import sys,os
from PIL import Image,ImageDraw
#二值化处理
def binary(im):
    pixels =im.load()
    for x in range(im.width):
        for y in range(im.height):
            pixels[x,y] = 255 if pixels[x,y]>125 else 0



#二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换
def getPixel(image,x,y,G,N):
    L = image.getpixel((x,y))
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0
    if L == (image.getpixel((x - 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x,y-1))
    else:
        return None

#降噪
#根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），
#当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
#参数解释：
#G: Integer 图像二值化阀值
#N: Integer 降噪率 0 <N <8
#Z: Integer 降噪次数
#输出0表示降噪成功,输出1表示降噪失败

def clearNoise(image,G,N,Z):
    draw = ImageDraw.Draw(image)

    for i in range(0,Z):
        for x in range(1,image.size[0] - 1):
            for y in range(1,image.size[1] - 1):
                color = getPixel(image,x,y,G,N)
                if color != None:
                    draw.point((x,y),color)

ori_path = 'E:\graduate_project\img'
file_path = 'E:\graduate_project\img_proc'
if not os.path.exists(ori_path):
    os.mkdir(ori_path)
if not os.path.exists(file_path):
    os.mkdir(file_path)


if __name__ == '__main__':
    for i in range(1,201):

        #先进行灰度化
        gray_im = Image.open((os.path.join(ori_path,'%d.png' %i))).convert('L')
        gray_im.save((os.path.join(file_path,'%d_g.png' %i)))

        #再进行去噪点操作
        noise_im = Image.open((os.path.join(file_path,'%d_g.png' %i)))
        clearNoise(noise_im,50,4,4)
        noise_im.save((os.path.join(file_path,'%d_n.png' %i)))

        #最后进行二值化
        binary_im = Image.open((os.path.join(file_path,'%d_n.png' %i)))
        binary(binary_im)
        binary_im.save((os.path.join(file_path,'%d_b.png' %i)))