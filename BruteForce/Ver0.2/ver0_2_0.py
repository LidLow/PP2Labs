#Version 0.2.0v
#What is new:
#   1) some syntax improvements;
#   2) answerList had been changed from list to set.

import random
import math
import time

def stringPermutation(string):
    answerList = set() #set to list -> ignoring duplicates automatically, so it won't take resources to check the list every time
    charList = list(string)
    numComb = math.factorial(len(string))

    while numComb != len(answerList):
        random.shuffle(charList)
        tempString = "".join(charList)
        answerList.add(tempString)

    return answerList

start_time = time.time()

print(stringPermutation("ABCDEFGHIJK"))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"The task took {elapsed_time:.2f} seconds to complete.")

#Some statistics: 
#   Uppercase letters, without duplicates:
#       <6!  -> 0.00 sec
#       6!   -> 0.01 sec
#       7!   -> 0.09 sec
#       8!   -> 1.44 sec
#       9!   -> 17.30 sec
#       10!  -> 176.82 sec
#       11!  -> 52 min
#       >11! -> ?