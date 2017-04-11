from PIL import Image
import os
import sys
from numpy import *
import numpy as np

ori_path = 'E:\graduate_project\sample'
file_path = 'E:\graduate_project\sample_txt'

if not os.path.exists(ori_path):
    os.mkdir(ori_path)
if not os.path.exists(file_path):
    os.mkdir(file_path)

for i in range(1,49):
    #先进行灰度化
    im=Image.open((os.path.join(ori_path,'%d.png' %i))).convert('L')
    #阈值设为200，数据归一化
    img=im.point(lambda p: p * 1.5) \
        .point(lambda p: 255 if p > 200 else 0) \
        .convert("1")
    width = img.size[0]
    height = img.size[1]
    print("/* width:%d */"%(width))
    print("/* height:%d */"%(height))
    lst=[]
    for h in range(0, height):
        for w in range(0, width):
            pixel = img.getpixel((w,h))
            lst.append(pixel)
    #黑点标记为1，无像素标记为0
    Len=len(lst)
    for j in range(0,Len):
        if lst[j]==255:
            lst[j]=0
        elif lst[j]==0:
            lst[j]=1
    tmp_lst=[str(k) for k in lst]
    #向量写到txt和sample.py里面，便于以后对比
    with open((os.path.join(file_path,'%d.txt' %i)), 'w')as f:
        f.write(' '.join(tmp_lst))
'''
    with open((os.path.join(file_path,'sample.py')), 'a')as f:
        f.write('N[%d]=[' %i)
        n=0
        for id in range(0,len(tmp_lst)):
            if(n%width==0):
                f.write('\n')
            f.write(tmp_lst[id])
            f.write(',')
            n+=1

        f.write(']\n\n')
'''