import cv2 as cv
import numpy as np

img = cv.imread('detect_blob.png')
cv.imshow('shapes',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thr = cv.threshold(gray,240,255,cv.THRESH_BINARY)
contours = cv.findContours(thr,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)


for contours in contours:
    appx = cv.approxPolyDP(contours,0.01* cv.arcLength(contours,True),True)
    cv.drawContours(img,[appx],0,(0,0,0),5)
    x = appx.ravel()[0]
    y = appx.ravel()[1]
    if len(appx)==3:
        cv.putText(img,'Triangle',(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

cv.waitKey(0)
cv.destroyAllWindows()