import cv2

img = cv2.imread('pic.avif',)
#cv2.line(img,(200,200),(180,20),(0,0,255),3)
cv2.rectangle(img,(165,205),(52,20),(0,0,255),5)
cv2.circle(img,(110,110),110,(0,0,255),5)
cv2.putText(img, 'TRF', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
#cv2.boxFilter(img,-1,(3,3))
#cv2.GaussianBlur(img,(5,5),sigmaX=1,sigmaY=2)
#cv2.medianBlur(img,3)
ret, image = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('image',img)

#print("Type:",type(img)) 
#print("Image data type:", img.dtype) 
#print("Pixel Values: \n", len(img[0]))
#print("Dimension:", img.ndim)
#print("Shape of Image:", img.shape) 
#print("Total Number of pixels:", img.size)


key =cv2.waitKey(5000)

cv2.destroyAllWindows()