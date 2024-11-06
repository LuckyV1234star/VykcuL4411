import cv2
import time

cam_port = 0
cam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)

def capture():
    result, image = cam.read()
    file_name = f"\\img\\temp\\{time.asctime(time.localtime())}.jpg"

    if result:
        cv2.imwrite(file_name, image)
        return file_name