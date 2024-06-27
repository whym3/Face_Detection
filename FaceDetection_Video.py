import cv2

# Try using DirectShow backend if MSMF is causing issues
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    faces = faceCascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
