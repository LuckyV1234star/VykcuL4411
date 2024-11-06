import os
import time

def count(flight = "CX 524"): #assume a flight input
    plastic = len(os.listdir("./img/plastic"))
    can = len(os.listdir("./img/can"))
    tetra_pak = len(os.listdir("./img/tetra_pak"))
    other = len(os.listdir("./img/other"))

    for i in os.listdir("./img"):
        for j in os.listdir(f"./img/{i}"):
            os.remove(f"./img/{i}/{j}")

    file = open(f"./record/{flight} {time.strftime("%Y%m%d%H%M%S")}.txt", "w")
    file.write(f"Plastic:{plastic} Can:{can} Tetra:{tetra_pak} Other:{other}")
    
    return plastic, can, tetra_pak, other