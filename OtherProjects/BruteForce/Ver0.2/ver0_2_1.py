"""

import multiprocessing
import time
import math
import random

def stringPermutation(string, answerList):
    charList = list(string)
    numComb = math.factorial(len(string))

    while numComb != len(answerList):
        random.shuffle(charList)
        tempString = "".join(charList)
        answerList.add(tempString)

if __name__ == "__main__":
    start_time = time.time()
    
    string = input("Input: ")
    
    answerList = set()  # Shared list across processes
    
    p1 = multiprocessing.Process(target=stringPermutation, args=(string, answerList))
    p2 = multiprocessing.Process(target=stringPermutation, args=(string, answerList))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(answerList)  # Convert to set to remove duplicates

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"The task took {elapsed_time:.2f} seconds to complete.")

    """

#Version 0.2.1v
#First multiprocessing programm
#What is new:
#   1) imported multiprocessing library
#   2) 5 cores
#
#Critcal problems:
#   1) The code is from 0.1.0v, so it has low performance due to checking the list every time.
#   2) mp liblary doesn't support set()


import multiprocessing
import time
import math
import random

def stringPermutation(string, answerList):
    charList = list(string)
    numComb = math.factorial(len(string))

    while numComb != len(answerList):
        random.shuffle(charList)
        tempString = "".join(charList)
        
        if tempString not in answerList:
            answerList.append(tempString)

if __name__ == "__main__":
    start_time = time.time()
    
    string = input("Input: ")
    
    manager = multiprocessing.Manager()
    answerList = manager.list()  # Shared list across processes
    
    p1 = multiprocessing.Process(target=stringPermutation, args=(string, answerList))
    p2 = multiprocessing.Process(target=stringPermutation, args=(string, answerList))
    p3 = multiprocessing.Process(target=stringPermutation, args=(string, answerList))
    p4 = multiprocessing.Process(target=stringPermutation, args=(string, answerList))
    p5 = multiprocessing.Process(target=stringPermutation, args=(string, answerList))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    print(set(answerList))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"The task took {elapsed_time:.2f} seconds to complete.")

#Some statistics: 
#   Uppercase letters, without duplicates, 5 cores:
#       1!      ->  2.75 sec
#       2!      ->  1.82 sec
#       3!      ->  3.43 sec
#       4!      ->  3.79 sec
#       5!      ->  3.76 sec
#       6!      ->  7.87 sec
#       7!      ->  19.12 sec
#       8!      ->  255.86 sec
#       9!      ->  