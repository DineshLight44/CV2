import cv2 as c 

img = c.imread("Image filtering\9kj62y.jpg")

# syntx = blur = cv.medianblur(img,kernel size)

blur = c.medianBlur(img,11)
c.imshow("orginal",img)
c.imshow("blured",blur)
c.waitKey(0)
c.destroyAllWindows()