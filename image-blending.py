import cv2 as cv
import numpy as np

apple = cv.imread('apple.jpg')
org = cv.imread('orange.jpg')

apple_orange = np.hstack((apple[:,:256],org[:, 256:]))

# generate gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
# generate gaussian pyramid for apple
org_copy = org.copy()
gp_orange = [org_copy]

for i in range(6):
    org_copy = cv.pyrDown(org_copy)
    gp_orange.append(org_copy)
# generate laplacin pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5,0,-1):
    g_e = cv.pyrUp(gp_apple[i])
    laplacin = cv.subtract(gp_apple[i-1],g_e)
# generate laplacin pyramid for apple
org_copy = gp_orange[5]
lp_orange = [org_copy]
for i in range(5,0,-1):
    g_e = cv.pyrUp(gp_orange[i])
    laplacin = cv.subtract(gp_orange[i-1],g_e)

# Join left and right halves of thr images
apple_orange_py = []
n = 0
for apple_lap,org_lap in zip(lp_apple,lp_orange):
    n +=1
    cols,rows,ch = apple_lap.shape
    laplacin = np.hstack((apple_lap[:,0:int(cols/2)],org_lap[:,int(cols/2):]))
    apple_orange_py.append(laplacin)

# reconstruct
apple_orange_recon = apple_orange_py[0]
for i in range(1,6):
    apple_orange_recon = cv.pyrUp(apple_orange_recon)
    apple_orange_recon = cv.add(apple_orange_py[i],apple_orange_recon)



cv.imshow('Apple',apple)
cv.imshow('Orange',org)
cv.imshow('apple_Orange_Recon',apple_orange_recon)

cv.waitKey(0)
cv.destroyAllWindows()