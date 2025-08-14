import cv2 as cv
import numpy as np

img = cv.imread("Image filtering\image.png")
#syntex = cv.filter2D(src,depth(-1 = same as input),kernel)

sharp_karnel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharp = cv.filter2D(img,-1,sharp_karnel)

cv.imshow("Original image",img)
cv.imshow("shapr image",sharp)
cv.waitKey(0)
cv.destroyAllWindows()

