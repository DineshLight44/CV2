import cv2 as cv 

img = cv.imread('9kj62y.jpg')
## resized = cv2.resize(src, dsize, fx=0, fy=0, interpolation)

if img is None:
    print("Image not found")
else:
    print("image loaded")
    resized = cv.resize(img,(750,750))
    cv.imshow("original img",img)
    cv.imshow("resized image",resized)
    cv.waitKey(0)
    cv.destroyAllWindows()