import cv2 as cv
img = cv.imread('9kj62y.jpg')
if img is not None:
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    save = cv.imwrite('grayscale.jpg', gray)
    cv.imshow('grayscale.jpg', gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print("no image found")
    