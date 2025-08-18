import cv2 as cv
import numpy as np

img = cv.imread(r"Finding and drawing contours\\sample.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 200, 155, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0, 145, 240), 5)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    corners = len(approx)
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "UK"  # Unknown

    cv.drawContours(img, [approx], 0, (0, 255, 140), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv.putText(img, shape_name, (x, y), cv.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0))

cv.imshow("contours", img)
cv.waitKey(0)
cv.destroyAllWindows()
