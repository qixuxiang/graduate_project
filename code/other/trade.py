from numpy import *
import numpy as np
import os
file_path='E:/graduate_project/sample_txt'
if not os.path.exists(file_path):
    os.mkdir(file_path)
for i in range(1,49):
    #先从导出的txt里面加载数据
    b = np.loadtxt((os.path.join(file_path,'%d.txt')%i),delimiter=" ",dtype=int32)
    #规范化
    c =b.reshape(32,24)
    #print(b)
    #计算“投影”下来的1的数目
    d= np.sum(c,axis=0)
    lst=d.tolist()
    tmp_lst=[str(j) for j in lst]
    #写到sample01.py准备后面使用
    with open(os.path.join(file_path,'sample01.py'),'at') as f:
        f.write('[')
        f.write(', '.join(tmp_lst))
        f.write('],')
        f.write('\n')