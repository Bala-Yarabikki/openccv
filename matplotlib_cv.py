from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg',1)

cv.imshow('img',img)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.xticks([]),plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()