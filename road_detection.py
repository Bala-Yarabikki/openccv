import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def region_of_interest(img,vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,)*channel_count
    cv.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv.bitwise_and(img,mask)
    return masked_image

img = cv.imread('road1.png')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
#cv.imshow('Image',img)

print(img.shape)
h = img.shape[0]
w = img.shape[1]

roi = [
    (0,h),
    (w/2, h/2),
    (w,h)]


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny_image = cv.Canny(gray,100,200)
cropped_image = region_of_interest(img,
                                   np.array([roi],np.int32))


plt.imshow(canny_image)
plt.show()

