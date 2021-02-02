import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')

while(1):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow('Frame',frame)
        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break
        else:
            break
cap.release()
cv.destroyAllWindows()