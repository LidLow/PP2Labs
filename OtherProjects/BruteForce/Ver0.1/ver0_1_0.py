#First variant of the bruteforce "programm"

import random
import math
import time

def stringPermutation(string):
    answerList = [string]
    charList = [x for x in string]
    numComb = math.factorial(len(string)) 

    while numComb != len(answerList):
        random.shuffle(charList) 
        tempString = "".join(charList)

        if tempString not in answerList: #O(n^2) 
            answerList.append(tempString)

    return answerList

start_time = time.time()

print(stringPermutation("ABCDEFGH"))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"The task took {elapsed_time:.2f} seconds to complete.")


#Some statistics: 
#   Uppercase letter, without duplicates:
#       <6! -> 0.00 sec
#       6!  -> 0.05 sec
#       7!  -> 2.08 sec
#       8!  -> 156.89 sec, 137.61 sec
#       9!  -> above 2 hours (test was terminated)
#       >9! -> CPU will be cooked