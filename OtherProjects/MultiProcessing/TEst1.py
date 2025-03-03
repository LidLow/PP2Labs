from multiprocessing import *
import os

def testFunc():
    for i in range(0, 100):
        print(i)



if __name__ == "__main__":
    p = Process(target=testFunc(), args=())
    q = Process(target=testFunc(), args=())

    p.start()
    q.start()

    p.join()
    q.join()