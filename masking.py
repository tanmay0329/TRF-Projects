import cv2
import numpy as np

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error")
else:
    while True:
        ret, frame = cam.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_threshold = np.array([20, 100, 100])
        upper_threshold = np.array([40, 255, 255])
        # contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # c = max(contours, key=cv2.contourArea)
       
        # cv2.drawContours(hsv_frame, [c], 0, (0,255,0), 3)
        # cv2.imshow("Webcam", hsv_frame)
        # if cv2.waitKey(1) == ord(" "):
        #     break

        mask = cv2.inRange(hsv_frame, lower_threshold, upper_threshold)

        cv2.imshow("Webcam", mask)
        if cv2.waitKey(1) == ord(" "):
            break
 
cam.release()
cv2.destroyAllWindows()