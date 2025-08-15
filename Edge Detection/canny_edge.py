import cv2 as cv

img = cv.imread(r"Edge Detection\natural-fresh-purple-orchid-flower-116.jpg", cv.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found.")
    exit()

# Apply Canny edge detection
edges = cv.Canny(img, 60, 168)

# Show images
cv.imshow("Original", img)
cv.imshow("Edges", edges)

cv.waitKey(0)
cv.destroyAllWindows()

