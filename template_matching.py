import cv2 as cv
import numpy as np

img = cv.imread('messi.jpg')
img2 = cv.imread('messi_fac.png',0)
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
w, h  = img2.shape[::-1]

res = cv.matchTemplate(grey,img2,cv.TM_CCOEFF_NORMED)
print(res)

thres = 0.59
loc = np.where(res >= thres)
print(loc)
for pr in zip(*loc[::-1]):
    cv.rectangle(img,pr,(pr[0]+w,pr[1]+h),(0,0,255),2)

cv.imshow('Image',img)
#cv.imshow('Face',img2)

cv.waitKey(0)
cv.destroyAllWindows()
