# Write a Python code to accept a string from the user and display characters present at an even index number.

userInput = input()
print(f"Orginal String is {userInput}.\nPrinting only even index chars: ")

for i in range(0, len(userInput), 2):
    print(userInput[i])