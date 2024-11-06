import cv2
import time
import threading


cam_port = 0
cam = cv2.VideoCapture(cam_port)


result, image = cam.read()

if result:
    time.localtime
    cv2.imwrite(f"{time.asctime(time.localtime())}.jpg", image)
    