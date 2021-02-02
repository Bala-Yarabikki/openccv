import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('sudoku.png',0)
lap = cv.Laplacian(img,cv.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))
sobelx = cv.Sobel(img,cv.CV_64F,1,0)
sobely = cv.Sobel(img,cv.CV_64F,0,1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelcombine = cv.bitwise_xor(sobelx,sobely)



titles = ['image','lap','sobelX','sobelY','sobelcombine']
images = [img,lap,sobelx,sobely,sobelcombine]

for x in range(5):
    plt.subplot(2,3, x+1),plt.imshow(images[x],'gray')
    plt.title(titles[x])
    plt.xticks([]),plt.yticks([])
plt.show()
