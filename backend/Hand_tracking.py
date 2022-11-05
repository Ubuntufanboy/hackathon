import cv2
import mediapipe as mp
import time
import os
import math

cap = cv2.VideoCapture(0)
def detect_b():
    #160 100
    #40 210
    if distance(xvals,yvals,'THUMB_TIP') > 110:
        return False
    elif distance(xvals,yvals,'RING_TIP') < 190:
        return False
    elif distance(xvals,yvals,'INDEX_TIP') < 190:
        return False
    elif distance(xvals,yvals,'MIDDLE_TIP') < 190:
        return False
    elif distance(xvals,yvals,'PINKY_TIP') < 150:
        return False
    else:
        return True

global points
points = ["WRIST", "THUMB_BASE", "THUMB_BOTTOM", "THUMB_MIDDLE", "THUMB_TIP", "INDEX_BASE", "INDEX_BOTTOM", "INDEX_MIDDLE", "INDEX_TIP","MIDDLE_BASE", "MIDDLE_BOTTOM", "MIDDLE_MIDDLE", "MIDDLE_TIP", "RING_BASE", "RING_BOTTOM", "RING_MIDDLE", "RING_TIP", "PINKY_BASE", "PINKY_BOTTOM", "PINKY_MIDDLE", "PINKY_TIP"]
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
def distance(xvals, yvals, point: str):
    for i in range(21):
        if points[i] == point:
            id = i
    for i in range(21):
        if i == id:
            wrist = xvals[0], yvals[0]
            tip = xvals[id], yvals[id]
            return math.dist(wrist,tip) 
        else:
            continue

while True:
    xvals = []
    yvals = []
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                #print(points[id], cx, cy)
                xvals.append(cx)
                yvals.append(cy)
                if id ==4:
                    cv2.circle(img, (cx,cy), 7, (255,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    try:
        print(f"The distance between the pinky and the wrist is {distance(xvals,yvals,'THUMB_TIP')}")
        if detect_b():
            print("User is signing B!")
    except:
        pass
    cv2.imshow("Image", img)
    cv2.waitKey(1)
