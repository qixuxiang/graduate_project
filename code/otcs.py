from PIL import Image,ImageEnhance,ImageFilter,ImageDraw,ImageTk
def OtsuGray(image):
    # 创建Hist
    image = Image.open('E:/47_n.png')
    image.convert('L')
    hist = image.histogram()
    #print(len(hist))
    #print(hist)

    # 开始计算
    # 计算总亮度
    totalH = 0
    for h in range(0,256):
        v =hist[h]
        if v == 0 : continue
        totalH += v*h
        #print(h,totalH,v*h)
        

    width  = image.size[0]
    height = image.size[1]
    total  = width*height
    #print(width)
    #print(height)
    
    print("总像素:%d;总亮度:%d平均亮度:%0.2f"%(total,totalH,totalH/total))
    v = 0

    gMax = 0.0
    tIndex = 0
    
    # temp
    n0Acc = 0.0
    n1Acc = 0.0
    n0H   = 0.0
    n1H   = 0.0
    for t in range(1,255):
        v = hist[t-1]
        if v == 0: continue
        
        n0Acc += v          #灰度小于t的像素的数目
        n1Acc = total - n0Acc #灰度大于等于t的像素的数目
        n0H += (t-1)*v          #灰度小于t的像素的总亮度
        n1H = totalH - n0H  #灰度大于等于t的像素的总亮度

        if n0Acc > 0 and n1Acc > 0:
            u0 = n0H/n0Acc # 灰阶小于t的平均灰度
            u1 = n1H/n1Acc # 灰阶大于等于t的平均灰度
            w0 = n0Acc/total # 灰阶小于t的像素比例
            w1 = 1.0-w0      # 灰阶大于等于t的像素的比例
            uD = u0-u1
            g = w0 * w1 * uD * uD
            #print(t,u0,u1,w0,w1,g)
            if gMax < g:
                gMax = g
                tIndex = t           
    #print(tIndex) 
    return tIndex
if __name__ == '__main__':
    img=Image.open('E:/47_n.png')
    a=OtsuGray(img)
    print(a)
    img.show()
'''
    #enhancer = ImageEnhance.Contrast(im)
    otsu1=otsu.OtsuGray(image)
    #twoValue(image,200)
    print otsu1
    twoValue(image,otsu1)'''