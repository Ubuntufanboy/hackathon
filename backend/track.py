import cv2
import mediapipe as mp
import time
import os
import math

cap = cv2.VideoCapture(0)
def detect_a():
    #70 on pinky when doing A
    #Thumb must be more than 120
    if distance(xvals,yvals,"PINKY_TIP") > 88:
        return False
    elif distance(xvals,yvals,"RING_TIP") > 98:
        return False
    elif distance(xvals,yvals,"MIDDLE_TIP") > 98:
        return False
    elif distance(xvals,yvals,"INDEX_TIP") > 98:
        return False
    elif distance(xvals,yvals,"THUMB_TIP") < 150:
        return False
    else:
        return True
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
def detect_c():
    # Thumb must be at least 170 pixels away
    if distance(xvals,yvals,'THUMB_TIP') < 170:
        return False
    elif abs(distance(xvals,yvals,'PINKY_TIP') - distance(xvals,yvals,'RING_TIP')) > 40:
        return False
    elif abs(distance(xvals,yvals,'RING_TIP') - distance(xvals,yvals,'MIDDLE_TIP')) > 40:
        return False
    else:
        return True
def detect_d():
    if distance(xvals,yvals,'INDEX_TIP') < 140:
        return False
    elif distance(xvals,yvals,'THUMB_TIP') < 90:
        return False
    elif abs(distance(xvals,yvals,'RING_TIP') - distance(xvals,yvals,'MIDDLE_TIP')) > 20:
        return False
    else:
        return True
def detect_e():
    # Thumb should be 55
    if distance(xvals,yvals,'THUMB_TIP') > 65:
        return False
    elif distance(xvals,yvals,'THUMB_TIP') < 45:
        return False
    elif distance(xvals,yvals,'PINKY_TIP') > 98:
        return False
    elif distance(xvals,yvals,'RING_TIP') > 88:
        return False
    elif distance(xvals,yvals,'INDEX_TIP') > 98:
        return False
    elif distance(xvals,yvals,'MIDDLE_TIP') > 98:
        return False
    else:
        return True
def detect_f():
    if distance(xvals,yvals,'PINKY_TIP') < 260:
            return False
    elif distance(xvals,yvals,'RING_TIP') < 260:
        return False
    elif distance(xvals,yvals,'MIDDLE_TIP') < 260:
        return False
    elif distance(xvals,yvals,'INDEX_TIP') > 150:
        return False
    elif distance(xvals,yvals,'THUMB_TIP') > 150:
        return False
    else:
        return False
def detect_g():
    if distance(xvals,yvals,'INDEX_TIP') < 150:
        return False
    elif distance(xvals,yvals,'THUMB_TIP') < 100:
        return False
    elif distance(xvals,yvals,'PINKY_TIP') > 80:
        return False
    elif distance(xvals,yvals,'RING_TIP') > 90:
        return False
    elif distance(xvals,yvals,'MIDDLE_TIP') > 95:
        return False
    else:
        return True
def detect_h():
    if distance(xvals,yvals,'INDEX_TIP') < 320:
        return False
    elif distance(xvals,yvals,'MIDDLE_TIP') < 320:
        return False
    elif distance(xvals,yvals,'RING_TIP') > 180:
        return False
    elif distance(xvals,yvals,'MIDDLE_TIP') > 180:
        return False
    elif distance(xvals,yvals,'THUMB_TIP') > 170:
        return False
    else:
        return True
def detect_i():
    #220 70
    if distance(xvals,yvals,'PINKY_TIP') < 210:
        return False
    elif distance(xvals,yvals,'RING_TIP') > 75:
        return False
    elif distance(xvals,yvals,'INDEX_TIP') > 80:
        return False
    elif distance(xvals,yvals,'MIDDLE_TIP') > 90:
        return False
    elif distance(xvals,yvals,'THUMB_TIP') > 70:
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

while 1:
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
                if id ==20:
                    cv2.circle(img, (cx,cy), 7, (255,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    try:
        print(f"d for pinky {distance(xvals,yvals,'PINKY_TIP')}")
        print(f"d for ring {distance(xvals,yvals,'RING_TIP')}")
        #print(f"d for middle {distance(xvals,yvals,'MIDDLE_TIP')}")
        #print(f"d for index {distance(xvals,yvals,'INDEX_TIP')}")
        #print(f"d for thumb {distance(xvals,yvals,'THUMB_TIP')}")
        if detect_a():
            print("User is signing A!")
        if detect_b():
            print("User is signing B")
        if detect_c():
            print("User is signing C")
        if detect_d():
            print("User is signing D")
        if detect_e():
            print("User is signing E")
        if detect_f():
            print("USer is signing F")
        if detect_g():
            print("User is signing G")
        if detect_h():
            print("User is signing H")
        if detect_i():
            print("User is signing I")
    except Exception as e:
        print(e)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
