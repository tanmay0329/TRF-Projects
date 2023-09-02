import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to access the camera")
else:
    while True:
        ret, frame = cap.read()

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        import numpy as np

        # Lower HSV values for yellow
        lower_threshold = np.array([30, 100, 100])
        # Upper HSV values for yellow
        upper_threshold = np.array([60, 255, 255])


        mask = cv2.inRange(hsv_frame, lower_threshold, upper_threshold)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                frame_center_x = frame.shape[1] // 2
                
                if cX > frame_center_x:
                    print("Positive: Largest contour is on the right")
                else:
                    print("Negative: Largest contour is on the left")

            cv2.drawContours(frame, [c], 0, (0, 255, 0), 3)

        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) == ord(" "):
            break

cap.release()
cv2.destroyAllWindows()