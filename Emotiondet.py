# # import the required modules
# import cv2
# import matplotlib.pyplot as plt
# from deepface import DeepFace
  
# # read image
# img = cv2.imread('plotimg.jpeg')
  
# # call imshow() using plt object
# plt.imshow(img[:,:,::-1])
  
# # display that image
# plt.show()
  
# # storing the result
# result = DeepFace.analyze(img,actions=['emotion'])
  
# # print result
#print(result)
import cv2
import time
from deepface import DeepFace

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # Use the default camera (usually the built-in webcam)

# Set the time interval for analysis (5 minutes = 300 seconds)
analysis_interval = 10 # seconds

# Initialize the last analysis time
last_analysis_time = time.time()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Check if it's time to perform analysis
    current_time = time.time()
    if current_time - last_analysis_time >= analysis_interval:
        # Analyze the frame using DeepFace
        result = DeepFace.analyze(frame, actions=['emotion'])

        # Print the result
        print(result)

        # Update the last analysis time
        last_analysis_time = current_time

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()





