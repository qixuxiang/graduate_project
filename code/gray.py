from PIL import Image                          #导入PIL库
img = Image.open('scu.jpg').convert('L')	   #将picture.jpg进行灰度化
img.save('scu1.jpg')						   #灰度化后的文件保存为gray.jpg

