# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

a, b = int(input()), int(input())

if (a * b > 1000):
    print(a + b)
else:
    print(a * b)