from PIL import Image
import os
import sys
from numpy import *
import numpy as np
import operator
import datetime
import time
def SplitCharacter(Block):
    '''根据平均字符宽度找极小值点分割字符'''
    Pixels = Block.load()
    (Width, Height) = Block.size
    MaxWidth = 20 # 最大字符宽度
    MeanWidth = 14    # 平均字符宽度
    if Width < MaxWidth:  # 若小于最大字符宽度则认为是单个字符
        return [Block]
    Blocks = []
    PixelCount = []
    for i in range(Width):  # 统计竖直方向像素个数
        Count = 0
        for j in range(Height):
            if Pixels[i, j] == 0:
                Count += 1
        PixelCount.append(Count)
  
    for i in range(Width):  # 从平均字符宽度处向两侧找极小值点，从极小值点处进行分割
        if MeanWidth - i > 0:
            if PixelCount[MeanWidth - i - 1] > PixelCount[MeanWidth - i] < PixelCount[MeanWidth - i + 1]:
                Blocks.append(Block.crop((0, 0, MeanWidth - i + 1, Height)))
                Blocks += SplitCharacter(Block.crop((MeanWidth - i + 1, 0, Width, Height)))
                break
        if MeanWidth + i < Width - 1:
            if PixelCount[MeanWidth + i - 1] > PixelCount[MeanWidth + i] < PixelCount[MeanWidth + i + 1]:
                Blocks.append(Block.crop((0, 0, MeanWidth + i + 1, Height)))
                Blocks += SplitCharacter(Block.crop((MeanWidth + i + 1, 0, Width, Height)))
                break
    return Blocks
 
def SplitPicture(Picture):
    '''用连通区域法初步分隔'''
    Pixels = Picture.load()
    (Width, Height) = Picture.size
      
    xx = [0, 1, 0, -1, 1, 1, -1, -1]
    yy = [1, 0, -1, 0, 1, -1, 1, -1]
      
    Blocks = []
      
    for i in range(Width):
        for j in range(Height):
            if Pixels[i, j] == 255:
                continue
            Pixels[i, j] = 200
            MaxX = 0
            MaxY = 0
            MinX = Width
            MinY = Height
  
            # BFS算法从找(i, j)点所在的连通区域
            Points = [(i, j)]
            for (x, y) in Points:
                for k in range(8):
                    if 0 <= x + xx[k] < Width and 0 <= y + yy[k] < Height and Pixels[x + xx[k], y + yy[k]] == 0:
                        MaxX = max(MaxX, x + xx[k])
                        MinX = min(MinX, x + xx[k])
                        MaxY = max(MaxY, y + yy[k])
                        MinY = min(MinY, y + yy[k])
                        Pixels[x + xx[k], y + yy[k]] = 200
                        Points.append((x + xx[k], y + yy[k]))
  
            TempBlock = Picture.crop((MinX, MinY, MaxX + 1, MaxY + 1))
            TempPixels = TempBlock.load()
            BlockWidth = MaxX - MinX + 1
            BlockHeight = MaxY - MinY + 1
            for y in range(BlockHeight):
                for x in range(BlockWidth):
                    if TempPixels[x, y] != 200:
                        TempPixels[x, y] = 255
                    else:
                        TempPixels[x, y] = 0
                        Pixels[MinX + x, MinY + y] = 255
            TempBlocks = SplitCharacter(TempBlock)
            for TempBlock in TempBlocks:
                Blocks.append(TempBlock)
    return Blocks

if __name__ == '__main__':
    
    img=Image.open('E:/graduate_project/img_proc/1_b.png')
    lst=SplitPicture(img)
    for l in lst:
        l.show()







    '''
    ori_path = 'E:/graduate_project/img_cutcopy'
    file_path= 'E:/graduate_project/img_proc'

    if not os.path.exists(ori_path):
        os.mkdir(ori_path)
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    
    #for i in range(1,201):
     #   os.mkdir(os.path.join(ori_path,('%d') %i))
     
    for i in range(1,201):
        img=Image.open(os.path.join(file_path,('%d_b.png') %i))
        path=os.path.join(ori_path,('%d') %i)
        lst=SplitPicture(img)
        Len=len(lst)
        #for j in (0,Len-1):

        nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        j=int(nowTime)
        for k in lst:
            k.save(os.path.join(path,'%d.png'% j))
            time.sleep(0.1)
       '''      