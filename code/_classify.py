from PIL import Image
import os
import os.path
import shutil


file_path='E:\graduate_project\img_re'
num=sum([len(files) for root,dirs,files in os.walk(file_path)])
print(num)
'''
for i in range(1,231):
    make_path=os.path.join(file_path,'%d')%i
    if not os.path.exists(make_path):
        os.mkdir(make_path)
'''
name_lst=[]
lst=[]
#name_lst来存储文件名
for root, dirs, files in os.walk(file_path):
    for name in files:
        if name.endswith('.png'):
            lst.append(name[11:18])
        name_lst.append(name)

print(lst)
int_lst=[int(i) for i in lst]
#tmp用来标记每个图片结束的位置
tmp=[]
for i in range(0,len(int_lst)):
    if(int_lst[i]-int_lst[i-1]>1249):
        tmp.append(i)
#阈值在1400左右，此时元素个数恰好为200！
tmp.append(989)
print(tmp)
print(len(tmp))
key_list=list(range(1,num+1))
value_list=name_lst
my_dic=dict(zip(key_list,value_list))
print(my_dic)
