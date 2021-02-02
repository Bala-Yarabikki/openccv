import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('lena.jpg')
img = cv.cvtColor(img,cv.COLOR_BGRA2RGB)
kernal = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernal)
blur = cv.blur(img,(5,5))
gaus = cv.GaussianBlur(img,(5,5),0)
median = cv.medianBlur(img,5)
bifil = cv.bilateralFilter(img,9,75,75)

titles = ['image','2D conv','blur','Gaussianblur','median','bilateralFilter']
images = [img,dst,blur,gaus,median,bifil]

for x in range(6):
    plt.subplot(3,3, x+1),plt.imshow(images[x],'gray')
    plt.title(titles[x])
    plt.xticks([]),plt.yticks([])
plt.show()
