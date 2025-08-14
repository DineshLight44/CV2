import cv2 as cv

# syntex = img = cv.GaussianBlur(imgage,(kernel size x ,kernel size x),simga(how much blur strength) )

img = cv.imread("Image filtering\9kj62y.jpg")

blur = cv.GaussianBlur(img,(7,7),0)
cv.imshow("Original image",img)
cv.imshow("Blur image",blur)
cv.waitKey(0)
cv.destroyAllWindows()       