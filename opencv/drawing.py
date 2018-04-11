import numpy as np
import cv2

img=np.zeros((5,4,3), np.uint8)

cv2.line(img,(0,0),(511,511),(255,0,0),5)
samantha=cv2.imread("Samantha.jpg",0)
print img
cv2.imshow('summa',img)
cv2.waitKey(0)
x,y,channel=samantha.shape
print x,y,channel
#cv2.rectangle(img,())