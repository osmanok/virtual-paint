import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

colors = [
    [35, 100, 133, 128, 152, 255],
    [87, 95, 0, 152, 255, 255]
]


def find_color(img, colors):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in colors:
        lower = np.array(color[0][0:3])
        upper = np.array(color[0][3:6])
        mask = cv2.inRange(img_hsv, lower, upper)
        get_contours(mask)


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(img_result, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)


while True:
    success, img = cap.read()
    img_result = img.copy()
    find_color(img, colors)
    cv2.imshow("Result", img_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
