import cv2 as cv 
img  = cv.imread('drawing\9kj62y.jpg')

if img is not None:
    ##cv.putText(image, text, org, font, fontScale,color, thickness, lineType)
    cv.putText(img,"hello worold ",(250,250),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv.imshow("text",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("could not load img")