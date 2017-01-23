import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()

    cv2.imshow('Camera', frame)

    key = cv2.waitKey(30) & 0xff

    # Exit on escape
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()