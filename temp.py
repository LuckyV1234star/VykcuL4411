import os
import capturing
import recognition
import moving


if __name__ == "__main__":
    i = 0
    for file_name in os.listdir("./img/temp"):
        result = recognition.recognize(file_name)
        moving.file_moving(file_name, result)
        i += 1
        print(i)