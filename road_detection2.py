import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def region_of_interest(img,vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv.bitwise_and(img,mask)
    return masked_image

def draw_lines(img,lines):
    cpoy_img = np.copy(img)
    blank_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(blank_image,(x1,y1),(x2,y2),(0,255,0),3)
    img = cv.addWeighted(img,0.8,blank_image,1,0.0)
    return img

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
cropped_image = region_of_interest(canny_image,
                                   np.array([roi],np.int32))

lines = cv.HoughLinesP(cropped_image,
                       rho=6,
                       theta = np.pi/180,
                       threshold=160,
                       lines = np.array([]),
                       minLineLength = 40,
                       maxLineGap=25)

img_lines = draw_lines(img,lines)

plt.imshow(cropped_image)
plt.show()

