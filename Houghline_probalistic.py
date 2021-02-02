import cv2 as cv
import numpy as np
img = cv.imread('sudoku.png',)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 75, 150)
cv.imshow('edges',edges)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 200, minLineLength = 100, maxLineGap=10)
for lines in lines:
    x1,y1,x2,y2 = lines[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)



cv.imshow('Image',img)
k = cv.waitKey(0)
cv.destroyAllWindows()