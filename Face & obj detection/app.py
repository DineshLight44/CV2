import cv2 as cv

face_cascade = cv.CascadeClassifier(r"Face & obj detection\haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)  # Try 0 if 1 doesn't work

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit the loop if frame is not captured

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow("detection", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
