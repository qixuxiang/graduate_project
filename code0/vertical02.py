from PIL import Image
import os
import sys
from numpy import *
from pylab import *
import numpy as np
import operator
import pylab as pl
import matplotlib.pyplot as plt
def get_point(im):
    '''
    获取垂直投影图
    '''
    x,y = im.size

    Lim = im.convert('L')
    threshold = 200
    table = []
    for i in range(256):
        if i > threshold:
            table.append(0)
        else:
            table.append(1)

    # convert to binary image by the table
    bim = Lim.point(table, '1')
    bdata=bim.load()
    vertical_projection = {}
    for b in range(x):
        vertical_projection[b] = 0

    for a in range(y):
        for b in range(x):
            #print bdata[b,a],
            if bdata[b,a] == 1:
                vertical_projection[b] += 1
    y = 0
    for x in vertical_projection:
        #print(x, vertical_projection[x])
        if y < vertical_projection[x]: y = vertical_projection[x]
    return vertical_projection


if __name__ == '__main__':
    img=Image.open('E:/47_b.png')
    dic=get_point(img)

    x = list(dic.keys())# Make an array of x values
    y = list(dic.values())# Make an array of y values for each x value
    plt.plot(x, y)# use pylab to plot x and y
    plt.show()# show the plot on the screen
'''
    xx=np.arange(len(x))
    x1 = np.array(x)
    y1 = np.array(y)
    plt.figure()
    axe1=plt.axes([0.16,0.12,0.77,0.77])

    # make a histogram of the data array
    #plt.hist(data, num_bins, normed=1, facecolor='green', alpha=0.5)
    # make plot labels 
    axe1.bar(xx,y1,align='center', color='blue', alpha=0.5)
    #plt.xlabel('data',size=140,color='k')
    #axe1.set_yticks(xx)
    axe1.set_yticklabels(x)
    plt.show()
'''
