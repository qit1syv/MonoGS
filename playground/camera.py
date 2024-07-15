import cv2
import sys

cam = cv2.VideoCapture(0)

img_counter = 0

ret, frame = cam.read()
if not ret:
    print("failed to grab frame")
    sys.exit(1)

cv2.imwrite("test.png", frame)


cam.release()
