from multiprocessing import *
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
    
    manager = Manager()
    answerList = manager.dict() 

    with Process(5) as p:
        p = Process(target=stringPermutation, args=(string, answerList))
        p.start()

    for p in range (5):
        p.join()

    setList = set(answerList)
    
    print(set(answerList))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"The task took {elapsed_time:.2f} seconds to complete.")

#Some statistics: 
#   Uppercase letters, without duplicates, 5 cores:
#       1!      ->  
#       2!      ->  
#       3!      ->  
#       4!      ->  
#       5!      ->  
#       6!      ->  
#       7!      ->  
#       8!      ->  
#       9!      ->  