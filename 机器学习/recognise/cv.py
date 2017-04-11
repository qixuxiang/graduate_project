import cv2
image = cv2.LoadImage('test4.png')
b = cv2.CreateImage(cv.GetSize(image), image.depth, 1)
g = cv2.CloneImage(b)
r = cv2.CloneImage(b)
    
cv2.Split(image, b, g, r, None)
#cv.ShowImage('a_window', r)
cv2.imwrite('test4cv.png', gray)   
cv2 .WaitKey(0)