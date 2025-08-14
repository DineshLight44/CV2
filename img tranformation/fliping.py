import cv2 as cv
img = cv.imread('9kj62y.jpg')
if img is not None:
    flip_horizontal = cv.flip(img,1)  # 1 for horizontal flip
    flip_vertical = cv.flip(img,0)    # 0 for vertical flip
    flip_both = cv.flip(img,-1)      # -1 for both horizontal and vertical flip
    cv.imshow("orginal img is this",img)
    cv.imshow("horizontal flip ",flip_horizontal)
    cv.imshow("vertical flip",flip_vertical)
    cv.imshow("both flip",flip_both)
    cv.waitKey(0)
    cv.destroyAllWindows()