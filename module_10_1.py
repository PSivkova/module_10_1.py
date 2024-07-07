from threading import Thread
from time import sleep


def func1():
    for i in range(1, 11):
        print(i)
        sleep(1)


def func2():
    for i in range(97, 107):
        print(chr(i))
        sleep(1)


th1 = Thread(target=func1)
th2 = Thread(target=func2)
th1.start()
th2.start()
th1.join()
th2.join()
