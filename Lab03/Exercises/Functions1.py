#1
def gramsToOunces(grams):
    return grams * 28.3495231


#2
def FahrenheitTocelcius(F):
    return (F - 32) / 1.8


#3
def solve(numHeads, numLegs):
    numRabbits = (numLegs - 2 * numHeads) / 2
    numChicks = numHeads - numRabbits
    return numRabbits, numChicks


#4
def filter_prime(list):
    for x in list:
        counter = 0
        
        for i in range(1, x):
            if x % i == 0:
                counter += 1

        if counter > 2: 
            list.remove(x)
            x -= 1

    return list


#5      
def stringPermutation(string):
    import math
    import random

    answerList = set()
    charList = list(string)
    numComb = math.factorial(len(string))

    while numComb != len(answerList):
        random.shuffle(charList)
        tempString = "".join(charList)
        answerList.add(tempString)

    return answerList


#6
def reverseString(string):
    list = string.split()
    return list.reverse()


#7
def has_33(list):
    for i in range(len(list) - 1):
        if list[i] == list[i + 1] == 3:
            return True

    return False


#8
def spy_game(list):
    newList = [str(x) for x in list if x == 7 or x == 0]
        
    return "".join(newList).find("007") != -1


#9
def sphereVolume(radius):
    from math import pi

    return 4/3 * pi * radius**3


#10
def uniqueElements(list):
    list.sort()
    newList = []

    for x in list:
        if x not in newList:
            newList.append(x)

    return newList


#11
def isPalindrom(string):
    list = [x for x in string]
    list.reverse()

    return "".join(list).lower() == string.lower()


#12
def histogram(list):
    newList = ["*" * n for n in list]

    return "\n".join(newList)


#13 - "Guess the number"
import random

global userName
global conunter
randomInteger = random.randint(1, 20)

def guessTheNumber():
    gNum = int(input("Take a guess. "))
    counter = 1

    if gNum > randomInteger:
        print("Your guess is too high.")
    elif gNum < randomInteger:
        print("Your guess is too low.")
    else:
        print(f"Good job, {userName}! You guessed my number in {counter + 1} guesses!")
        exit()

    return guessTheNumber()

userName = input("Hello! What is your name? ")
print(f"Well, {userName}, I am thinking of a number between 1 and 20.")
guessTheNumber()