# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

a = b = 0

for a in range(0, 10):
    print(f"Current Number {a} Previous Number {b}  Sum: {a + b}")
    b = a