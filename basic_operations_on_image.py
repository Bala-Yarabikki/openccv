import numpy as np
import cv2

img = cv2.imread('cam.jpg',1)
img1 = cv2.imread('lena.jpg',1)
print(img.size)
print(img.shape)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

img = cv2.resize(img,(512,512))
img1 = cv2.resize(img1,(512,512))

#new = cv2.add(img,img1)
new = cv2.addWeighted(img,.8,img1,.2,0)

cv2.imshow('image',new)
cv2.waitKey(0)
cv2.destroyAllWindows()