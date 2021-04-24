import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('Resources\haarcascades\haarcascade_frontalface_default.xml')


while True:
    success, img = cap.read()
    faces = faceCascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
