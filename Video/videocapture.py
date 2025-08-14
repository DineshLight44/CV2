import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret,fram = cap.read()
    if not ret:
        print("could not read frame")
        break

    cv.imshow("webcam",fram)

    if cv.waitKey(1) & 0xFF == ord('q'):
        print("quit")
        break

cap.release()
cv.destroyAllWindows()