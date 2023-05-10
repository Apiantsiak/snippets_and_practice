import threading as thr
import time

VALUE = 0
locker = thr.RLock()


def increase_val(n):
    global VALUE
    print(f"{thr.current_thread().name}: acquired")
    with locker:
        VALUE += 1
        print(f"val => {VALUE}")
        print(f"{thr.current_thread().name}: released")


for i in range(5):
    thr.Thread(target=increase_val, args=(i,)).start()

print("Done")
