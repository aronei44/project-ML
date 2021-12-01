from handDetection import HandDetection
import cv2
import math
from pymouse import PyMouse
import numpy as np
import keyboard

monitor_height = 768
monitor_width = 1366

handDetection = HandDetection(min_detection_confidence=0.5,min_tracking_confidence=0.5)


webcam = cv2.VideoCapture()
webcam.open(0,cv2.CAP_DSHOW)

m = PyMouse()

timer = 10

while True:
    if timer > 0:
        timer -= 1
    status, frame = webcam.read()
    frame = cv2.flip(frame,1)
    handLandMarks = handDetection.findHandLandMarks(image=frame, draw=True)

    if len(handLandMarks) != 0:
        x4, y4 = handLandMarks[4][1],handLandMarks[4][2]
        x5, y5 = handLandMarks[5][1],handLandMarks[5][2]
        x8, y8 = handLandMarks[8][1],handLandMarks[8][2]
        x9, y9 = handLandMarks[9][1],handLandMarks[9][2]
        x12, y12 = handLandMarks[12][1],handLandMarks[12][2]

        pos_x = x4*monitor_width/frame.shape[1]
        pos_y = y4*monitor_height/frame.shape[0]

        index = math.hypot(x5-x8,y5-y8)
        middle = math.hypot(x9-x12,y9-y12)
        # print(index)
        if timer <=0:
            if index <50:
                m.click(int(pos_x), int(pos_y),1)
                # index = 49
                timer =  10

            if middle < 50:
                m.click(int(pos_x), int(pos_y),2)
                timer =  10

        m.move(int(pos_x), int(pos_y))
        


    cv2.imshow("Hand Landmark", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
webcam.release()