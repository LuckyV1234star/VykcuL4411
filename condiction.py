import time
bottles = []
cans = []
tetraPak =[]
others = []
if result == bottle:
    print("push bottle")
    bottles.append("bottle")
elif result == metal:
    time.sleep(1)
    print("push metal")
    cans.append("metal")
elif result == tetra:
    time.sleep(2)
    print("push tetra")
    tetraPak.append("tetra")
else:
    time.sleep(3)
    print("push unknown")
    others.append("unknown")