import cv2 as cv
import numpy
# syntex = contours , hierarchy = cv.findContours(img,mode,method)

# img = binary (b/w)

# mode = 2 type = 1 = cv.RETR_LIST 2ND cv.RETR_EXTERNA
# cv.RETR_EXTERNAL:
# Finds only the outermost contours.
# If there are objects within other objects, only the outer boundaries are found.
# will find only the square’s outline.

# cv.RETR_TREE:
# Finds all contours and reconstructs the full hierarchy of nested contours.
# Useful if you have objects within objects and want to know which contours are inside others..
# will find both and tell you that the circle is inside the square.

# cv.CHAIN_APPROX_NONE:
# Keeps every single point along the contour.
# Good if you need all details, but uses lots of memory.

# cv.CHAIN_APPROX_SIMPLE:
# Compresses the contour, storing only essential points.
# Removes all redundant points—so you get fewer points, and use less memory.



# img = cv.imread(r"Finding and drawing contours\sample.jpg")
# #gray  = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# _, thresh = cv.threshold(img,200,155,cv.THRESH_BINARY)
# contours ,  heriy = cv.findContours(img,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# # cv.drawContours(img,contours,contour_index,colr, thickness)
# cv.drawContours(img,contours,-1,(0,145,240), 5)
# cv.imshow("contours",img)
# cv.waitKey(0)
# cv.destroyAllWindows()


img = cv.imread(r"Finding and drawing contours\\sample.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 200, 155, cv.THRESH_BINARY)

contours, heriy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0, 145, 240), 5)
for contour in contours:
    approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour),True)
    corners = len(approx)
    if corners ==3:
        shape_name = "Triangle"

    elif corners ==4:
        shape_name = "rectangle"

    elif corners ==5:
        shape_name = "pentagon"

    elif corners >5:
        shape_name = "circle"

    else:
        shape_name = "UK"

    cv.drawContours(img,[approx],0,(0,255,140),2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv.putText(img,shape_name,(x,y),cv.FONT_HERSHEY_COMPLEX,0.6,(0,255,0))
cv.imshow("contours", img)
cv.waitKey(0)
cv.destroyAllWindows()
