import cv2
def empty(a):
    pass
import numpy as np

img = cv2.imread("S1.jpg")
cv2.namedWindow("Colour")
cv2.resizeWindow("Colour", 640, 240)

cv2.createTrackbar("Hue_Min", "Colour", 0, 179, empty)
cv2.createTrackbar("Hue_Max", "Colour", 0, 179, empty)
cv2.createTrackbar("Sat_Min", "Colour", 0, 255, empty)
cv2.createTrackbar("Sat_Max", "Colour", 0, 255, empty)
cv2.createTrackbar("Val_Min", "Colour", 0, 255, empty)
cv2.createTrackbar("Val_Max", "Colour", 0, 255, empty)



while True:
    img = cv2.imread("S1.jpg")
    img2 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h_min = cv2.getTrackbarPos("Hue_Min", "Colour")
    h_max = cv2.getTrackbarPos("Hue_Max", "Colour")
    s_min = cv2.getTrackbarPos("Sat_Min", "Colour")
    s_max = cv2.getTrackbarPos("Sat_Max", "Colour")
    v_min = cv2.getTrackbarPos("Val_Min", "Colour")
    v_max = cv2.getTrackbarPos("Val_Max", "Colour")
    print (h_min, h_max, s_min, s_max, v_min, v_max)

    lower=np.array([h_min, s_min, v_min])
    upper=np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img2, lower, upper)
    img_res = cv2.bitwise_and(img,img, mask=mask)


    cv2.imshow("result", img_res)
    cv2.imshow("mask", mask)
    cv2.waitKey(1)
