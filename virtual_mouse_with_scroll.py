
import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import math

wScr, hScr = pyautogui.size()
frameR = 100
smoothening = 5
plocX, plocY = 0, 0
clocX, clocY = 0, 0

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

def fingersUp(lmList):
    fingers = []
    tipIds = [4, 8, 12, 16, 20]
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)
    for id in range(1, 5):
        if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmList = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1], lmList[8][2]
        x2, y2 = lmList[12][1], lmList[12][2]
        fingers = fingersUp(lmList)

        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, 640 - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, 480 - frameR), (0, hScr))
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            pyautogui.moveTo(clocX, clocY)
            plocX, plocY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:
            length = math.hypot(x2 - x1, y2 - y1)
            if length < 40:
                pyautogui.click()

        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0:
            pyautogui.scroll(5)

        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 1:
            pyautogui.scroll(-5)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
