import cv2 as cv 
img = cv.imread('drawing\9kj62y.jpg')

if img is not None:
    ## cv.circle(image, center_coordinates, radius, color, thickness)
    cv.circle(img,(150,244),50,(255,0,0),5)    ## if thickness == -1: whole circle will be fill    cv.imshow('circle', img)
    cv.waitKey(0)           
    cv.destroyAllWindows()
else:
    print("could not load img")