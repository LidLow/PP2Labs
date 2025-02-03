import os
import re

os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab05\Exercises")

sample = open("sample.txt", "r", encoding="UTF-8")
catalogue = sample.read()


#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
def fromAtoB():     
    return re.findall("\w*аб+\w*", catalogue)


#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def fromAtoB2():
    return re.findall("\w*аб{2,3}\w*", catalogue) 


#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
def underscoreConn():
    return re.findall()


#4. Write a Python program to find the sequences of one uppercase letter followed by lower case letters.




#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def endsOnAB(): return re.findall("\w*аб", catalogue)






















#Testing section
print(endsOnAB())