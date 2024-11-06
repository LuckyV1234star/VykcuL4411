import os

def count():
    plastic = len(os.listdir("./img/plastic"))
    can = len(os.listdir("./img/can"))
    tetra_pak = len(os.listdir("./img/tetra_pak"))
    other = len(os.listdir("./img/other"))

    return plastic, can, tetra_pak, other