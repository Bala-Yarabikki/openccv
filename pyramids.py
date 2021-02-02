import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i),layer)
ayer = gp[5]
cv.imshow('upperlevel',layer)
lp = [layer]

for i in range(5,0,-1):
    g_ex = cv.pyrUp(gp[i])
    

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()