import cv2
import numpy as np

width=400

height=400

channels=3

custom_image = np.zeros((height, width, channels))


for y in range(height): 
    for x in range(width): 
        custom_image[y, x] = [255, 0, 255]

img = custom_image

#cv2.line(img,(200,200),(180,20),(0,0,255),3)
cv2.rectangle(img,(165,205),(52,20),(0,0,255),5)
cv2.circle(img,(110,110),110,(0,0,255),5)
cv2.putText(img, 'TRF', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("Custom Image", custom_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()