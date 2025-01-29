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
        answerList[tempString] = 0

if __name__ == "__main__":
    start_time = time.time()
    
    string = input("Input: ")
    
    manager = multiprocessing.Manager()
    answerList = manager.dict() 
    
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

    setList = set(answerList)
    
    print(set(answerList))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"The task took {elapsed_time:.2f} seconds to complete.")

#Some statistics: 
#   Uppercase letters, without duplicates, 5 cores:
#       1!      ->  1.79 sec
#       2!      ->  2.51 sec
#       3!      ->  3.48 sec
#       4!      ->  4.28 sec
#       5!      ->  9.11 sec
#       6!      ->  q
#       7!      ->  
#       8!      ->  
#       9!      ->  