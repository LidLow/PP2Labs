#1. Create a generator that generates the squares of numbers up to some number N.
def squareGenerator(num):
    for x in range(1, num+1):
        yield x**2


#2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def evenGenerator(num):
    for x in range(0, num+1):
        if x % 2 == 0:
            yield x

"""
num = int(input("Input: "))

obj = evenGenerator(num)
print(next(obj))
print(next(obj))
"""


#3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisiblesDenerator(num):
    for x in range(0, num+1):
        if x % 4 == 0 and x % 3 == 0:
            yield x


#4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def abSquareGenerator(a, b):
    for x in range(a, b+1):
        yield x**2

"""
obj = abSquareGenerator(5, 8)

for x in obj:
    print(x)
"""


#5. Implement a generator that returns all numbers from (n) down to 0.
def upToDownGenerator(num):
    for x in range(num, -1, -1):
        yield x


#Testing section

obj = upToDownGenerator(6)

for x in obj:
    print(x)