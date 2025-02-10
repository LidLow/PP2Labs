import os
import re

os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab05\Exercises")

sample = open("sample.txt", "r", encoding="UTF-8")
catalogue = sample.read()


#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
def fromAtoB(string):
    return re.findall("\w*ab*\w*", string)


#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def fromAtoB2(string):
    return re.findall("\w*ab{2,3}\w*", string) 


#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
def underscoreConn(string):
    return re.findall(r"\w*_[a-z]+", string)


#4. Write a Python program to find the sequences of one uppercase letter followed by lower case letters.
def upLower(string):
    return re.findall("[A-Z][a-z]+", string)


#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def endsOnAB(string):
    return re.findall("\w*a\w*b$", string)


#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def replaceToColon(string):
    return re.sub("[,.\s]", ":", string)


#7. Write a python program to convert snake case string to camel case string.
def snakeToCamel(string):
    return re.sub(r"(_)([a-z])", lambda c: c.group(2).upper(), string)


#8. Write a Python program to split a string at uppercase letters.
def splitAtUpper(string):
    return re.split("[A-Z][a-z]+", string)
    

#9. Write a Python program to insert spaces between words starting with capital letters.
def spaceBetweenThem(string):
    return re.sub(r"([A-Z][a-z]+) ([A-Z][a-z]+)", r"\1   \2", string)


#10. Write a Python program to convert a given camel case string to snake case.
def camelToSnake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()


#Testing section
print(snakeToCamel(catalogue))