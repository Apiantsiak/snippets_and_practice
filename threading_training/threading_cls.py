import time
from threading import Thread


class CountdownThread(Thread):

    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.n - i - 1, "left")
            time.sleep(1)


t = CountdownThread(3)
t_1 = CountdownThread(3)
t.start()
t_1.start()


# better implementatuon

class CountdownThread:

    def __init__(self, n):
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.n - i - 1, "left")
            time.sleep(1)


t = CountdownThread(3)
t_1 = CountdownThread(3)
t.start()
t_1.start()
