import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('Samantha.jpg',1)
#cv2.namedWindow('darling',cv2.WINDOW_NORMAL)
img
cv2.imshow('darling',img)
k=cv2.waitKey(0)&0XFF
if k==ord('q'):
    cv2.destroyAllWindows()
    print img
b,g,r=cv2.split(img)
img2=cv2.merge([r,g,b])
plt.imshow(img2)
plt.xticks([]);plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()