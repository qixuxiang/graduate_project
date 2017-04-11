'''
@Author qixuxiang
@Date 2016.03.08
cutgraph.py
图片切割并规范化成24*32图片，利于后面提取特征值
'''
from PIL import Image
from numpy import *
import os
import datetime
import time


ori_path = 'E:\graduate_project\img_proc'
file_path = 'E:\graduate_project\img_cut'
re_path = 'E:\graduate_project\img_re'
if not os.path.exists(ori_path):
    os.mkdir(ori_path)
if not os.path.exists(file_path):
    os.mkdir(file_path)
if not os.path.exists(re_path):
    os.mkdir(re_path)   
#图片x轴的投影，如果有数据（黑色像素点）值为1否则为0
def get_projection_x(image):
    p_x = [0 for x in range(image.size[0])]
    for w in range(image.size[1]):
        for h in range(image.size[0]):
            if image.getpixel((h,w)) == 0:
                p_x[h] = 1
    length=len(p_x)

    return p_x

'''测试函数
def count_size(im):
    print(im.size)
'''

#获取分割后的x轴坐标点
#返回值为[起始位置, 长度] 的列表
def get_split_seq(projection_x):
    res = []
    for idx in range(len(projection_x) - 1):
        p1 = projection_x[idx]
        p2 = projection_x[idx + 1]
        if p1 == 1 and idx == 0:
            res.append([idx, 1])
        elif p1 == 0 and p2 == 0:
            continue
        elif p1 == 1 and p2 == 1:
            res[-1][1] += 1
        elif p1 == 0 and p2 == 1:
            res.append([idx + 1, 1])
        elif p1 == 1 and p2 == 0:
            continue
    return res

#分割后的图片，x轴分割后，同时去掉y轴上线多余的空白
def split_image(image, split_seq=None):
    if split_seq is None:
        split_seq = get_split_seq(get_projection_x(image))
    length = len(split_seq)
    imgs = [[] for i in range(length)]
    res = []
    for w in range(image.size[1]):
        line = [image.getpixel((h,w)) for h in range(image.size[0])]
        for idx in range(length):
            pos = split_seq[idx][0]
            llen = split_seq[idx][1]
            l = line[pos:pos+llen]
            imgs[idx].append(l)
    for idx in range(length):
        datas = []
        height = 0
        for data in imgs[idx]:
            flag = False
            for d in data:
                if d == 0:
                    flag = True
            if flag == True:
                height += 1
                datas += data

                #print(datas)
                #print(len(datas))
        #二值化图片被切割后被规范化为24*32的图片
        child_img = Image.new('L',(split_seq[idx][1], height))
        child_img.putdata(datas)
        #生成了时间戳，不重复随机数，精确到微秒
        nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        j=int(nowTime)
        child_img.save(os.path.join(file_path,'%d_.png' % (j)))
        img=Image.open(os.path.join(file_path,'%d_.png' % (j)))
        new_img = img.resize((24,32),Image.BILINEAR)
        new_img.save(os.path.join(re_path,'%d.png'% (j)))
        time.sleep(0.1)
        res.append(child_img)
    return res



if __name__ == '__main__':

    for i in range(1,201):
        img = Image.open((os.path.join(ori_path,'%d_b.png' %i)))
        #count_size(Image.open('1b.png'))
        get_projection_x(img)
        get_split_seq('px')
        split_image(img)