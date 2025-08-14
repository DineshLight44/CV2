import cv2 as cv 
img = cv.imread('9kj62y.jpg')
if img is not None:
    CROP = img[100:400, 100:400]  # Example crop coordinates
    cv.imshow("orginal imag",img)
    cv.imshow("after crop",CROP)
    cv.waitKey(0)
    cv.destroyAllWindows()