#1. Write a Python program with builtin function to multiply all the numbers in a list
def func_1(list):
    sum = 1

    for i in range(len(list)):
        sum *= list[i]

    return sum


#2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def func_2(string):
    numLower= 0

    for x in string:
        if x.lower() == x:
            numLower += 1

    return numLower, len(string) - numLower


#3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def func_3(string):
    list = [x for x in string]
    list.reverse()

    return "".join(list).lower() == string.lower()


#4. Write a Python program that invoke square root function after specific milliseconds.
def func_4(number, milsec):  
    __import__("time").sleep(milsec / 1000)     #О Великий Python Docs
    
    return f"Square root of {number} after {milsec} miliseconds is {pow(number, 0.5)}"
    

#5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
def func_5(tuple):
    for b in tuple:
        if not b:
            return b
        

#Testing section
print(func_4(25, 5))