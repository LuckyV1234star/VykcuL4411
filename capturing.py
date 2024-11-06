import cv2
import time
import threading


cam_port = 0
cam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)

result, image = cam.read()

if result:
    cv2.imshow(f"{time.asctime(time.localtime())}", image)
    cv2.imwrite(f"\\img\\{time.asctime(time.localtime())}.jpg", image)

    cv2.waitKey(0)