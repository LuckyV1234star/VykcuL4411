import os
import time

recycle = {
    "塑膠":"plastic",
    "紙包飲品":"tetra_pak",
    "金屬製品":"can",
    "其他":"other"
}

time_trans = {
    "塑膠":0,
    "紙包飲品":2,
    "金屬製品":1,
    "其他":3
}

def file_moving(file_name,result):
    os.rename(f"./img/temp/{file_name}",f"./img/{recycle[result]}/{file_name}")
    print(f"push {recycle[result]}")
    time.sleep(time_trans[result])