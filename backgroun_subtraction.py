import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')
#fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv.createBackgroundSubtractorKNN()

while cap.isOpened():
    ret,frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    cv.imshow('Frame',frame)
    cv.imshow('FG_MASK_Frame',fgmask)

    key = cv.waitKey(30)
    if key=='q' or key  == 27:
        break
cap.release()
cv.destroyAllWindows()