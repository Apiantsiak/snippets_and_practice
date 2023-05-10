import time
import threading as thr


def print_word(word, iters):
    print(thr.enumerate())
    for i in range(1, iters + 1):
        print(i, word)
        # time.sleep(0.5)


t_1 = thr.Thread(target=print_word, args=("Hello", 3))
t_2 = thr.Thread(target=print_word, args=("world", 3))
print(t_1.name)
t_1.start()
print(t_1.ident)
t_1.join()

print(t_2.name)
t_2.start()
print(t_1.is_alive())
print(t_2.ident)
t_2.join()

print("MainThread finished!")
