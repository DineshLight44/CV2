# import cv2 as cv 

# img = cv.imread('9kj62y.jpg')

# if img is not None:
#     h,w,c = img.shape
#     print(f"img shape is \nheight:{h} \nwidth:{w} \nchannel:{c}")

# else:
#     print("could not load img")

import cv2 as cv 

img = cv.imread('9kj62y.jpg')

if img is not None:
    h,w,c = img.shape
    print(f"img shape is \nheight:{h} \nwidth:{w} \nchannel:{c}")

else:
    print("could not load img")