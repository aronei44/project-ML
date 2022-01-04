import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    # flip windows
    frame = cv2.flip(frame,1)

    # display the resulting frame
    cv2.imshow('frame',frame)

    # triger to exit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()