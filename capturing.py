import cv2
import time



def capture():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)
    result, image = cam.read()
    file_name = f"{time.strftime("%Y%m%d%H%M%S")}.jpg"

    if result:
        cv2.imwrite(f"./img/temp/{file_name}", image)
        return file_name