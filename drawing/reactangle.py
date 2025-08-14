import cv2 as cv 
img = cv.imread('drawing\9kj62y.jpg')
if img is not None:
    pt1 = (100, 100)
    pt2 = (200, 200)
    cv.rectangle(img,pt1,pt2,(0, 255, 180),3)
    cv.imshow('rectangle', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("could not load img")
