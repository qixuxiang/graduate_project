from PIL import Image
from numpy import *
import numpy as np
if __name__ == '__main__':
	img=Image.open('E:/47_n.png')
	img_arr = array(img,'f')
	#print(img_arr)
	#print(img_arr.dtype,img_arr.size,img_arr.shape)
	img_arr1=img_arr.reshape(img_arr.size)
	#print(img_arr1)
	print(np.mean(img_arr1))
