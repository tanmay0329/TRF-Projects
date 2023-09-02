import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error : Unabel to access the camera")

else:
    while True:
        ret, frame = cap.read()

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_threshold = np.array([20,50,50])
        upper_threshold = np.array([40,255,255])

        mask = cv2.inRange(hsv_frame, lower_threshold, upper_threshold)
        # img_contour = mask.copy()

        contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # for cnt in contours:
        #     cv2.drawContours(hsv_frame, [cnt], 0,(0, 255, 0),3)

        c = max(contours, key=cv2.contourArea, default=0)
       
        # cv2.drawContours(frame, [c], 0, (0,0,0), 3)

        # M = cv2.moments(c) 
        # cX = int(M["m10"] / M["m00"])
        # cY = int(M["m01"] / M["m00"])   
        # print(cX , cY)

        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cX = x+(w/2)
        cY = y+(h/2)
        # print(cX,',',cY) 
        fY = frame.shape[0]//2
        fX = frame.shape[1]//2
        # print(fX,fY) 
        x = fX // 100
        if(cX<fX):
            
            y = - int((fX-cX)/x) 
            print(y)
        elif(cX>fX):
            
            z = int((cX-fX)/x)
            print(z)
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) == ord(" "):
            break

cap.release()
cv2.destroyAllWindows()