#1
class MyString:
    def setString(self): #setter
        self.string = input("Input: ")

    def getString(self): #getter
        print(self.string.upper())

"""user = MyString()
user.setString()
user.getString()"""


#2
class Shape:
    def __init__(self, length):
        self.length = length
        self.area = 0

    def getArea(self):
        return self.area

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
        self.area = Shape.getArea(self.length)

    def setArea(self):
        self.area = self.length  * self.length

    def getAreaSquare(self):
        return self.area
    

#4
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

    def dist(self, xSecAxis, ySecAxis):
        return round(math.sqrt((xSecAxis - self.xAxis)**2 + (ySecAxis - self.yAxis)**2), 2)
    

#5
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
            return True
        
        return False
    

#6
def filter_prime(n):
    counter = 0

    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1

        if counter > 2: 
            return False

    return True

list = [2, 3, 5, 9, 11]

isPrime = lambda n: filter_prime(n)
answerList = filter(filter_prime, list)

for x in answerList:
    print(x)