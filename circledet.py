import cv2
import numpy as np

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in laptop camera)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for red color (in HSV)
    lower_red = np.array([0, 100, 50])    # Adjust these values for your specific shade of red
    upper_red = np.array([10, 255, 255]) # Adjust these values for your specific shade of red

    # Create a mask for the red color range
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # Define the lower and upper bounds for blue color (in HSV)
    lower_blue = np.array([90, 50, 50])    # Adjust these values for your specific shade of blue
    upper_blue = np.array([130, 255, 255]) # Adjust these values for your specific shade of blue

    # Create a mask for the blue color range
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Combine the red and blue masks
    mask = mask_red | mask_blue

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Use the Hough Circle Transform to detect circles in the mask
    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=30,          # Increase this value for circles that are closer to each other
        param1=100,          # Increase for better circle detection (may need adjustment)
        param2=30,           # Increase for more robust circle detection (may need adjustment)
        minRadius=100,       # Minimum circle radius in pixels (adjust for 20 cm diameter)
        maxRadius=120        # Maximum circle radius in pixels (adjust for 20 cm diameter)
    )

    # If circles were found, draw them on the original frame
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            cv2.circle(frame, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)
            cv2.circle(frame, (circle[0], circle[1]), 2, (0, 255, 0), 3)

    # Display the frame with detected circles
    cv2.imshow('Circles Detected', frame)

    # Exit the loop when the ' ' key is pressed
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

