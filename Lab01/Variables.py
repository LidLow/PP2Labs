#Python Variables

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
print(type(y))


#Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#Assign Multiple Values

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Output Variables

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#Global Variables

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)


#Variable Exercises
#I have already done all the exercises in that subtopic