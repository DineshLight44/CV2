import cv2 as cv 

img = cv.imread('9kj62y.jpg')
if img is not None:
    success = cv.imwrite('saved_image.jpg', img)
    if success:
        print("Image saved successfully as'saved_image.jpg'")
    else:
        print("failed to save image")
    