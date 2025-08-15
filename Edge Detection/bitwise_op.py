# cv.bitwise_and(img1, img2): Cuts out the shape from one image using another (intersection of both images).

# cv.bitwise_or(img1, img2): Combines everything from both images (merges multiple images).

# cv.bitwise_not(img1): Inverts (negates) the pixel values of the image (creates a negative).

# img1 img2 hight and width should be same
# use only b/w img



import numpy as np
import cv2 as cv

img1 = np.zeros((300,300),dtype="uint8")
img2 = np.zeros((300,300),dtype="uint8")

cv.circle(img1,(150,150),100,255,-1)
cv.rectangle(img2,(100,100),(250,250),255,-1)

bitwise_and = cv.bitwise_and(img1,img2)
bitwise_or = cv.bitwise_or(img1,img2)
bitwise_not = cv.bitwise_not(img1)

cv.imshow("circle",img1)
cv.imshow("recangle",img2)

cv.imshow("AND",bitwise_and)
cv.imshow("or",bitwise_or)
cv.imshow("not",bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()