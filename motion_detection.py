import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()




while cap.isOpened():
    diff = cv.absdiff(frame1,frame2)
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    _,thr = cv.threshold(blur,20,255,cv.THRESH_BINARY)
    dia = cv.dilate(thr,None,iterations = 3)
    contour,_ = cv.findContours(dia,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for contour in contour:
        (x,y,w,h) = cv.boundingRect(contour)
        
        if cv.contourArea(contour) < 900:
            continue
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(frame1,"Status: {}".format('Movement'),(10,20),cv.FONT_HERSHEY_SIMPLEX,
                   1,(255,0,0),3)

    #cv.drawContours(frame1,contour,-1,(0,255,0),2)
    
    
    cv.imshow('feed',frame1)
    frame1 = frame2
    ret,frame2 = cap.read()
    if cv.waitKey(40) == 27:
        break

cap.release()
cv.destroyAllWindows()