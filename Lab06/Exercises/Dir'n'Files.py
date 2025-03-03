import os

os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab06\Exercises")

#1. Write a Python program to list only directories, files and all directories, files in a specified path.
def func_1(path):
    listCurrentDir = [child.name for child in os.scandir('./') ]
    listCustomDir = [child.name for child in os.scandir(path) ]

    return listCurrentDir, listCustomDir


#2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def func_2(path):
    return ("Existance:", os.access()), ("Readability;", os.access(path, os.R_OK)), ("Writability:", os.access(path, os.W_OK)), ("Executability:", os.access(path, os.X_OK))
    

#3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def func_3(path):
    if os.path.exists(path):
        return os.path.dirname(path), os.path.basename(path)
    else:
        return "Error"


#4. Write a Python program to count the number of lines in a text file.
def func_4(textFile):
    with open(textFile, "r", encoding="utf-8") as file:
        return sum(1 for line in file)


#5. Write a Python program to write a list to a file.
def func_5(textFile, list):
    with open(textFile, "a") as file:
        file.write(str(list))

    return True


#6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
from string import ascii_uppercase as auc

def func_6():
    for c in auc:
        file = open(f"{c}.txt", "x")

    return True


#7. Write a Python program to copy the contents of a file to another file
import shutil

def func_7(file):
    defaultPath = os.getcwd()
    
    shutil.copy2(file, defaultPath)
    return True

#8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def func_8(path):
    if os.path.exists(path) and os.access(path, os.F_OK):
        os.remove(path)
        return True
    else:
        return False


#Testing section
print()