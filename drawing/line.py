import cv2 as cv

img = cv.imread("drawing\9kj62y.jpg")
if img is not None:
    pt1 = (250,100)
    pt2= (400,100)
    
    col = (250,0,0)
    thickness = 5
    cv.line(img, pt1, pt2, col, thickness)
    cv.imshow("line", img)
    cv.waitKey(0)                               
    cv.destroyAllWindows()
else:
    print("could not load img")