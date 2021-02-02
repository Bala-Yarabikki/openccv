import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('gr.png',0)

_,th = cv.threshold(img,70,255,cv.THRESH_BINARY)
_,th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img,150,255,cv.THRESH_TRUNC)
_,th4 = cv.threshold(img,150,255,cv.THRESH_TOZERO)
_,th5 = cv.threshold(img,150,255,cv.THRESH_TOZERO_INV)

titles = [1,2,3,4,5,6]
images = [img,th,th2,th3,th4,th5]

for x in range(6):
    plt.subplot(2,3,x+1),plt.imshow(images[x],'gray')
    plt.title(titles[x])
    plt.xticks([]),plt.yticks([])


#cv.imshow('img',img)
#cv.imshow('th',th)
#cv.imshow('th2',th2)
#cv.imshow('th3',th3)
#cv.imshow('th4',th4)
#cv.imshow('th5',th5)

#cv.waitKey(0)
#cv.destroyAllWindows()
plt.show()

