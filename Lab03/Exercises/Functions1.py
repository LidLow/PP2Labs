#1. A recipe you are reading states how many grams you need for the ingredient. 
#   Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. 
def gramsToOunces(grams):
    return grams * 28.3495231


#2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
#   The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def FahrenheitTocelcius(F):
    return (F - 32) / 1.8


#3. Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
#   How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numHeads, numLegs):
    numRabbits = (numLegs - 2 * numHeads) / 2
    numChicks = numHeads - numRabbits
    return numRabbits, numChicks


#4. You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
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


#5. Write a function that accepts string from user and print all permutations of that string.     
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


#6. Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def reverseString(string):
    list = string.split()
    return list.reverse()


#7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(list):
    for i in range(len(list) - 1):
        if list[i] == list[i + 1] == 3:
            return True

    return False


#8. Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(list):
    newList = [str(x) for x in list if x == 7 or x == 0]
        
    return "".join(newList).find("007") != -1


#9. Write a function that computes the volume of a sphere given its radius.
def sphereVolume(radius):
    from math import pi

    return 4/3 * pi * radius**3


#10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def uniqueElements(list):
    list.sort()
    newList = []

    for x in list:
        if x not in newList:
            newList.append(x)

    return newList


#11. Write a Python function that checks whether a word or phrase is palindrome or not. 
#    Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def isPalindrom(string):
    list = [x for x in string]
    list.reverse()

    return "".join(list).lower() == string.lower()


#12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
#    For example, histogram([4, 9, 7]) should print the following:
def histogram(list):
    newList = ["*" * n for n in list]

    return "\n".join(newList)


#13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
#    This is how it should work when run in a terminal:
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