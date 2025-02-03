#1. Define a class which has at least two methods: getString - to get a string from console input printString - to print the string in upper case.
class MyString:
    def setString(self): #setter
        self.string = input("Input: ")

    def getString(self): #getter
        print(self.string.upper())


#2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
#   Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
    def __init__(self, length):
        self.length = length
        self.area = 0

    def getArea(self):
        return self.area

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
        self.area = Shape.getArea(self)

    def setArea(self):
        self.area = self.length**2


#3. Define a class named Rectangle which inherits from Shape class from task 2. 
#   Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Shape:
    def __init__(self, length):
        self.length = length
        self.area = 0

    def getArea(self):
        return self.area

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
        self.area = Shape.getArea(self)

    def setArea(self):
        self.area = self.length  * self.width


#4. Write the definition of a Point class. Objects from this class should have a
#      1) a method show to display the coordinates of the point
#      2) a method move to change these coordinates
#      3) a method dist that computes the distance between 2 points
import math

class Point():
    def __init__(self): #default constructor
        self.xAxis = 0
        self.yAxis = 0

    def move(self, xAxis, yAxis): #initializing variables
        self.xAxis = xAxis
        self.yAxis = yAxis

    def show(self): #getter
        print(f"X: {self.xAxis}, Y: {self.yAxis}")

    def dist(self, xSecAxis, ySecAxis): #distance between (x1;y1) and (x2;y2)
        return round(math.sqrt((xSecAxis - self.xAxis)**2 + (ySecAxis - self.yAxis)**2), 2)
    

#5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
#   Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class BankAccount():
    def __init__(self): #default
        self.owner = "N/A"
        self.balance = 0
    
    def __init__(self, owner, balance): 
        self.owner = owner
        self.balance = balance

    def deposit(self, amountOfReplenishment): #++money to balance
        self.balance += amountOfReplenishment 

    def withdraw(self, amountOfWithdrawal): #--money from balance
        if self.balance >= amountOfWithdrawal:
            self.balance -= amountOfWithdrawal
            return "Success."
        
        return "Not enough funds."
    

#6. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
def filter_prime(n):
    counter = 0

    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
        if counter > 2: 
            return False

    return True

list = [2, 3, 5, 9, 11, 13, 15, 16]

isPrime = lambda n: filter_prime(n)
answerList = filter(isPrime, list)

for x in answerList:
    print(x)