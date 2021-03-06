from PIL import Image
import os
import sys
from numpy import *
import numpy as np
import operator

file_path = 'E:\graduate_project\img_re'

if not os.path.exists(file_path):
    os.mkdir(file_path)

def getFile_dict():
    num=sum([len(files) for root,dirs,files in os.walk(file_path)])
    print(num)
    name_lst=[]
    lst=[]
    #name_lst来存储文件名
    for root, dirs, files in os.walk(file_path):
        for name in files:
            if name.endswith('.png'):
                lst.append(name[11:18])
            name_lst.append(name)
    #print(lst)
    int_lst=[int(i) for i in lst]
    #tmp用来标记每个图片结束的位置
    tmp=[]
    for i in range(0,len(int_lst)):
        if(int_lst[i]-int_lst[i-1]>1249):
            tmp.append(i)
    #阈值在1400左右，此时元素个数恰好为200！
    tmp.append(989)
    #print(tmp)
    #print(len(tmp))
    key_list=list(range(1,num+1))
    value_list=name_lst
    dic=dict(zip(key_list,value_list))
    return dic

def img2vector(im):

    #阈值设为200，数据归一化
    img=im.point(lambda p: p * 1.5) \
    .point(lambda p: 255 if p > 200 else 0) \
    .convert("1")
    width = img.size[0]
    height = img.size[1]
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
    data = np.array(lst).reshape(32,24)
    d = np.sum(data,axis=0)
    data_lst=d.tolist()
    return data_lst


def classify0(inX,dataSet,labels,k):
    #先计算各自的欧氏距离
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffmat=pow(diffMat,2)
    sqDistance=sqDiffmat.sum(axis=1)
    distances=sqDistance**0.5
    sortedDisIndicies=distances.argsort()
    classCount={}
    #排序欧式距离最小的前K个数
    for i in range(k):
        voteIlable=labels[sortedDisIndicies[i]]
        classCount[voteIlable]=classCount.get(voteIlable,0)+1
    sortedClassCount=sorted(classCount.items(),
                            key=operator.itemgetter(1),reverse=True)
    #距离最小的即是最可能的结果
    return sortedClassCount[0][0]



N=[]
for i in range(49):
    N.append([])


N[1]=[8, 8, 11, 11, 11, 11, 12, 12, 13, 32, 32, 32, 32, 32, 32, 6, 5, 4, 4, 4, 4, 4, 4, 4]
N[2]=[12, 11, 13, 13, 13, 14, 12, 13, 12, 12, 13, 12, 13, 12, 13, 13, 13, 14, 16, 15, 15, 12, 11, 9]
N[3]=[6, 6, 8, 12, 14, 13, 14, 14, 13, 13, 13, 12, 11, 16, 16, 17, 19, 19, 25, 22, 22, 18, 16, 15]
N[4]=[4, 6, 7, 9, 10, 14, 14, 14, 10, 11, 12, 11, 12, 31, 31, 29, 29, 32, 32, 4, 4, 4, 4, 4]
N[5]=[3, 20, 21, 23, 23, 22, 21, 15, 14, 13, 12, 12, 12, 13, 14, 18, 16, 18, 22, 21, 19, 17, 16, 13]
N[6]=[14, 15, 17, 24, 26, 18, 18, 17, 15, 14, 13, 13, 13, 14, 15, 16, 18, 20, 22, 21, 18, 12, 10, 9]
N[7]=[4, 4, 4, 7, 9, 10, 13, 13, 13, 14, 14, 14, 11, 10, 11, 7, 8, 9, 12, 12, 11, 8, 7, 6]
N[8]=[5, 8, 9, 19, 22, 25, 27, 26, 18, 14, 15, 13, 15, 13, 14, 18, 24, 25, 24, 22, 13, 8, 7, 6]
N[9]=[6, 9, 10, 17, 19, 18, 17, 16, 12, 11, 12, 11, 11, 12, 11, 12, 13, 15, 15, 19, 21, 15, 14, 6]
N[10]=[12, 14, 20, 23, 13, 12, 12, 14, 12, 10, 8, 8, 8, 8, 10, 13, 13, 12, 12, 13, 22, 20, 18, 14]
N[11]=[8, 9, 10, 21, 23, 24, 20, 19, 18, 20, 21, 21, 18, 17, 14, 29, 30, 31, 29, 29, 28, 7, 6, 6]
N[12]=[32, 32, 32, 32, 32, 31, 12, 10, 9, 9, 10, 9, 8, 11, 12, 15, 16, 16, 21, 20, 19, 17, 15, 15]
N[13]=[9, 17, 19, 21, 21, 13, 12, 14, 13, 14, 13, 9, 8, 8, 9, 8, 8, 9, 9, 8, 9, 7, 7, 7]
N[14]=[15, 15, 17, 19, 20, 21, 14, 14, 14, 12, 11, 9, 9, 9, 9, 8, 8, 9, 31, 32, 32, 32, 32, 31]
N[15]=[18, 18, 22, 24, 25, 27, 28, 25, 24, 23, 19, 18, 18, 18, 19, 18, 18, 22, 22, 20, 18, 19, 17, 17]
N[16]=[4, 5, 5, 6, 28, 28, 29, 29, 31, 31, 31, 31, 12, 10, 9, 9, 9, 9, 8, 7, 4, 4, 3, 3]
N[17]=[13, 14, 14, 21, 24, 23, 19, 19, 16, 13, 13, 12, 9, 14, 13, 14, 17, 17, 28, 29, 28, 28, 28, 26]
N[18]=[31, 32, 32, 32, 32, 31, 4, 3, 2, 2, 3, 3, 4, 5, 5, 4, 4, 4, 23, 24, 24, 23, 23, 22]
N[19]=[27, 27, 27, 27, 27, 28, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 31, 30, 30, 30, 30, 30]
N[20]=[3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 5, 6, 5, 5, 23, 24, 29, 29, 29, 28, 24, 24]
N[21]=[30, 32, 32, 32, 30, 3, 2, 2, 6, 7, 8, 8, 9, 8, 8, 9, 9, 6, 5, 6, 6, 4, 3, 2]
N[22]=[18, 19, 23, 28, 28, 30, 31, 31, 28, 25, 23, 5, 5, 5, 5, 5, 6, 6, 6, 5, 4, 4, 3, 3]
N[23]=[32, 32, 31, 10, 10, 14, 14, 13, 12, 11, 5, 12, 14, 16, 14, 15, 10, 10, 32, 32, 32, 28, 29, 28]
N[24]=[29, 32, 32, 32, 32, 30, 4, 4, 5, 5, 5, 4, 6, 6, 6, 7, 7, 7, 31, 31, 31, 29, 29, 27]
N[25]=[10, 21, 22, 26, 27, 24, 20, 20, 18, 12, 12, 12, 12, 14, 14, 18, 20, 20, 25, 26, 25, 20, 20, 15]
N[26]=[29, 30, 31, 31, 31, 29, 8, 8, 7, 8, 9, 8, 8, 9, 8, 10, 12, 12, 14, 14, 14, 10, 9, 9]
N[27]=[12, 13, 15, 17, 17, 17, 13, 12, 12, 10, 9, 8, 8, 9, 9, 8, 9, 11, 31, 32, 32, 32, 32, 29]
N[28]=[24, 24, 30, 31, 31, 31, 31, 28, 28, 24, 6, 6, 6, 6, 5, 4, 5, 5, 6, 6, 6, 6, 5, 5]
N[29]=[9, 9, 14, 15, 16, 19, 19, 17, 16, 16, 16, 16, 15, 16, 17, 17, 18, 18, 19, 16, 13, 14, 14, 14]
N[30]=[5, 5, 6, 7, 8, 28, 29, 29, 30, 30, 32, 32, 32, 32, 13, 12, 12, 11, 11, 12, 12, 11, 10, 10]
N[31]=[25, 27, 28, 29, 29, 8, 7, 6, 4, 4, 4, 4, 4, 4, 5, 5, 6, 7, 8, 29, 28, 27, 26, 24]
N[32]=[6, 7, 7, 17, 16, 19, 19, 20, 17, 16, 15, 7, 7, 15, 16, 17, 20, 19, 19, 16, 17, 9, 8, 6]
N[33]=[7, 10, 24, 23, 22, 20, 7, 20, 22, 21, 16, 6, 6, 21, 22, 22, 16, 7, 18, 22, 25, 25, 11, 7]
N[34]=[6, 9, 10, 14, 17, 20, 20, 23, 23, 16, 12, 12, 12, 13, 14, 20, 22, 20, 18, 18, 16, 8, 8, 7]
N[35]=[4, 5, 5, 11, 11, 15, 15, 16, 21, 20, 20, 10, 9, 11, 11, 12, 12, 11, 11, 11, 11, 5, 5, 3]
N[36]=[12, 15, 16, 17, 17, 19, 19, 16, 16, 17, 17, 18, 17, 18, 19, 19, 18, 19, 18, 17, 16, 17, 14, 13]
N[37]=[4, 5, 12, 13, 15, 15, 15, 19, 20, 19, 18, 10, 10, 17, 19, 20, 19, 14, 14, 15, 12, 12, 5, 4]
N[38]=[2, 30, 30, 30, 31, 31, 31, 19, 17, 13, 14, 14, 15, 16, 19, 25, 24, 24, 23, 21, 16, 9, 7, 6]
N[39]=[26, 31, 32, 31, 29, 8, 8, 8, 8, 7, 8, 8, 10, 12, 13, 14, 15, 14, 21, 21, 19, 13, 12, 1]
N[40]=[31, 31, 31, 31, 32, 32, 15, 14, 12, 12, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 9, 9, 9, 7]
N[41]=[28, 30, 32, 32, 32, 26, 22, 10, 9, 9, 9, 9, 8, 8, 7, 7, 7, 9, 10, 9, 7, 4, 4, 3]
N[42]=[14, 16, 20, 22, 24, 15, 15, 16, 15, 13, 10, 8, 9, 10, 9, 8, 9, 9, 9, 18, 19, 20, 18, 16]
N[43]=[19, 32, 32, 32, 20, 6, 5, 5, 4, 4, 4, 4, 4, 5, 5, 5, 6, 4, 5, 27, 31, 31, 30, 23]
N[44]=[31, 32, 32, 32, 32, 8, 7, 9, 9, 9, 7, 8, 7, 7, 10, 10, 9, 7, 8, 32, 32, 32, 32, 31]
N[45]=[1, 9, 11, 17, 20, 12, 12, 11, 10, 8, 7, 7, 7, 7, 12, 16, 17, 16, 23, 22, 19, 16, 2, 1]
N[46]=[30, 30, 30, 30, 30, 11, 11, 9, 10, 11, 12, 14, 18, 21, 20, 19, 17, 14, 15, 5, 5, 4, 4, 2]
N[47]=[3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 32, 32, 32, 32, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
N[48]=[2, 2, 7, 8, 9, 11, 11, 8, 8, 8, 19, 19, 19, 19, 8, 8, 7, 11, 10, 8, 8, 7, 3, 2]

if __name__=='__main__':
    #自己建个字典
    my_dic={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'0',
            11:'a',12:'b',13:'c',14:'d',15:'e',16:'f',17:'g',18:'h',19:'i',
            20:'j',21:'k',22:'l',23:'m',24:'n',25:'o',26:'p',27:'q',28:'r',
            29:'s',30:'t',31:'u',32:'v',33:'w',34:'x',35:'y',36:'z',37:'A',
            38:'B',39:'D',40:'E',41:'F',42:'G',43:'H',44:'N',45:'Q',46:'R',
            47:'T',48:'Y'}
    '''
    img=Image.open(os.path.join(file_path,'20160322105007842816.png' )).convert('L')
    img1=Image.open(os.path.join(file_path,'20160322105007842816.png' )).convert('L')
    img2=Image.open(os.path.join(file_path,'20160322105007952184.png' )).convert('L')
    img3=Image.open(os.path.join(file_path,'20160322105008061570.png' )).convert('L')
    img4=Image.open(os.path.join(file_path,'20160322105008170946.png' )).convert('L')
    img5=Image.open(os.path.join(file_path,'20160322105008280322.png' )).convert('L')
    l1=img2vector(img1)
    l2=img2vector(img2)
    l3=img2vector(img3)
    l4=img2vector(img4)
    l5=img2vector(img5)
    

    group=array(N[1:49])
    labels=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
            22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,
            40,41,42,43,44,45,46,47,48]
    print("识别结果为：")
    print(my_dic.get(classify0(l1,group,labels,2)),my_dic.get(classify0(l2,group,labels,2)),my_dic.get(classify0(l3,group,labels,2)),my_dic.get(classify0(l4,group,labels,2)),
        my_dic.get(classify0(l5,group,labels,2)))
        '''
    pic_dict=getFile_dict();
    group=array(N[1:49])
    labels=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
            22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,
            40,41,42,43,44,45,46,47,48]
    print("识别结果为：")
    for i in range(1,len(pic_dict)+1):
        file_name=pic_dict.get(i)
        img=Image.open(os.path.join(file_path,file_name )).convert('L')
        l=img2vector(img)
        result=my_dic.get(classify0(l,group,labels,1))
        with open(os.path.join('E:/graduate_project/img_cut','result.txt'),'w') as f:
            f.write(result)
            f.write('\n')



        
