import cv2 as cv

img = cv.imread(r"Edge Detection\natural-fresh-purple-orchid-flower-116.jpg",cv.IMREAD_GRAYSCALE)

retun, thres_img = cv.threshold(img,135,255,cv.THRESH_BINARY)


cv.imshow("Original", img)
cv.imshow("THRESHOLD IMG", thres_img)

cv.waitKey(0)
cv.destroyAllWindows()

 