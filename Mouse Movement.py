import cv2
import time
import pyautogui as ptg
import numpy as np


def empty(a):
    pass

web = cv2.VideoCapture(0)
#web.set(3,1920)
#web.set(4,1080)


cv2.namedWindow("Colour")
cv2.resizeWindow("Colour", 690, 290)
cv2.createTrackbar("Hue_Min", "Colour", 0, 179, empty)
cv2.createTrackbar("Hue_Max", "Colour", 179, 179, empty)
cv2.createTrackbar("Sat_Min", "Colour",0, 255, empty)
cv2.createTrackbar("Sat_Max", "Colour", 12, 255, empty)
cv2.createTrackbar("Val_Min", "Colour", 255, 255, empty)
cv2.createTrackbar("Val_Max", "Colour", 255, 255, empty)

while True:
    success, imgg = web.read()
    img = cv2.flip(imgg, 1)

    img1=cv2.resize(img, (1920, 1080))
    img_b=cv2.GaussianBlur(img1, (5, 5), 0)
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue_Min", "Colour")
    h_max = cv2.getTrackbarPos("Hue_Max", "Colour")
    s_min = cv2.getTrackbarPos("Sat_Min", "Colour")
    s_max = cv2.getTrackbarPos("Sat_Max", "Colour")
    v_min = cv2.getTrackbarPos("Val_Min", "Colour")
    v_max = cv2.getTrackbarPos("Val_Max", "Colour")

    lower=np.array([h_min, s_min, v_min])
    upper=np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img2, lower, upper)
    img_res = cv2.bitwise_and(img1,img1, mask=mask)
    contours, _ = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>5000:
            print (cnt, type(cnt))


            goTo = cnt[0][0]
            x_val = goTo.item(0)
            y_val = goTo.item(1)
            """Line to uncomment"""
            # ptg.moveTo(x_val, y_val)  """Moves mouse to a position"""
            # ptg.click() """Clicks the mouse"""






    cv2.imshow("original", img)
    cv2.imshow("result", img_res)
    cv2.imshow("mask", mask)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        exit()

    cv2.waitKey(1)
