import time
import threading as thr

max_thr = 2
pool = thr.Semaphore(value=max_thr)


def take_break():
    with pool:
        slp = 2
        print(f"{thr.current_thread().name} - sleep {slp} sec.")
        time.sleep(slp)


for _ in range(4):
    thr.Thread(target=take_break).start()
