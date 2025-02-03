from multiprocessing import *
import os

def testFunc():
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())



if __name__ == "__main__":
    p = Process(target=testFunc(), args=())
    q = Process(target=testFunc(), args=())

    p.start()
    q.start()

    p.join()
    q.join()
