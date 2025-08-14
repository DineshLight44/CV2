import cv2 as cv

cam = cv.VideoCapture(0)

frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

cod = cv.VideoWriter_fourcc(*'XVID')
recorder = cv.VideoWriter("my_video.mp4", cod, 20, (frame_width, frame_height))

while True:
    succes, img = cam.read()
    if not succes:
        break

    recorder.write(img)
    cv.imshow("record live", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
recorder.release()
cv.destroyAllWindows()
