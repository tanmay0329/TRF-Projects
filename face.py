import cv2
import numpy as np

# Load the hat image
hat = cv2.imread('hat.jpg')

if hat is None:
    print("Error: Could not load the hat image.")
    exit()

# Load a pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Error: Could not load the face cascade classifier.")
    exit()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Resize the hat image proportionally to the face size
        hat_resized = cv2.resize(hat, (w, int(h * hat.shape[1] / hat.shape[0])))

        # Calculate the position to overlay the hat
        y_offset = y - int(hat_resized.shape[0] * 0.3)  # Adjust the y position for better placement
        x1 = x
        x2 = x + w
        y1 = y_offset
        y2 = y_offset + hat_resized.shape[0]

        # Overlay the hat on the frame using cv2.addWeighted to blend
        frame[y1:y2, x1:x2] = cv2.addWeighted(frame[y1:y2, x1:x2], 1, hat_resized, 0.8, 0)

    cv2.imshow('AR Masked Face', frame)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
