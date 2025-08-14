import cv2 as cv 

img = cv.imread(r'C:\Users\dkglt\OneDrive\Desktop\CV2\img\lisa-genshin-impact-uhdpaper.com-8K-3.3029.jpg')

if img is not None:
    cv.imshow("Loaded Image", img)  # Show the image in a window
    cv.waitKey(0)
    cv.destroyAllWindows()  
else:
    print("Image not loaded successfully")
