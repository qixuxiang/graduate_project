'''
@Author qixuxiang
@Date 2016.03.01
load_im.py
验证码图片下载和尺寸调整
'''
import urllib.request
import os
from PIL import Image


url = 'http://passport.csdn.net/ajax/verifyhandler.ashx'
ori_path = 'E:\graduate_project\img'
if not os.path.exists(ori_path):
	os.mkdir(ori_path)
if __name__ == '__main__':
	for i in range(1,201):
		#csdn验证码下载
		with open((os.path.join(ori_path,'%d_ori.png' %i)), 'wb') as f:
			f.write(urllib.request.urlopen(url).read())
		#调整图片大小
		img = Image.open((os.path.join(ori_path,'%d_ori.png' %i)))
		img.resize((140,45),Image.ANTIALIAS).save(os.path.join(ori_path,'%d.png' %i))

	'''img=Image.open(StringIO(urllib.request.urlopen(
		'http://passport.csdn.net/ajax/verifyhandler.ashx%d' %i).read()))


	img.save(os.path.join('E:\graduate_project','img','%d.png' % i))
	img.close()
	'''

