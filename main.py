import os
import capturing
import recognition
import moving
import counting

if __name__ == "__main__":
    file_name = capturing.capture()
    result = recognition.recognize(file_name)
    moving.file_moving(file_name, result)

    print(counting.count())