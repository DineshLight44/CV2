import cv2 as cv 

## m = cv.getRotationMatrix2D(center, angle,scale)  
##  roated_img = cv.warpAffine(img, m, (w, h))
img = cv.imread('9kj62y.jpg')
if img is not None:
    (h,w) = img.shape[:2]
    center = (w//2,h//2)
    M = cv.getRotationMatrix2D(center,70,1.0)
    rote = cv.warpAffine(img,M,(w,h))
    cv.imshow("before roatation",img)
    cv.imshow("after roatation",rote)
    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print("could not load img")