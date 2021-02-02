import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('s.png',0)

_,mask = cv.threshold(img,220,255,cv.THRESH_BINARY_INV)

kernal = np.ones((5,5),np.uint8)
dia = cv.dilate(mask,kernal,iterations=2)
ero = cv.erode(mask,kernal,iterations = 1)



titles = [1,2,3,4]
images = [img,mask,dia,ero]

for x in range(4):
    plt.subplot(1,4, x+1),plt.imshow(images[x],'gray')
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

