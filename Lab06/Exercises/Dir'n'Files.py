import os
from pathlib import *


#1. Write a Python program to list only directories, files and all directories, files in a specified path.
def func_1(directory):
    return os.listdir(directory)


#2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def func_2(directory):
    if Path.is_file(directory):
        Path.open(directory)
        Path.dir


#3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.



#4. Write a Python program to count the number of lines in a text file.



#5. Write a Python program to write a list to a file.



#6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt



#7. Write a Python program to copy the contents of a file to another file



#8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.



#Testing section
print(func_2(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab01"))