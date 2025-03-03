"""
n is 10

1) a = 1; tempNum = list[i - 1] + (1 / 2**i)
2) a = 2; tempNum = (-1)**(n+1) * list[i - 1] / 2
3) a1 = 1, a2 = 1; tempNum = list[i - 2] + list[i - 1]
"""

a1 = int(input("Enter the first term: "))
a2 = int(input("Enter the second term: "))
n = int(input("Number of terms: "))

list = []
list.append(a1)
list.append(a2)

for i in range(2, n):
    tempNum = list[i - 2] + list[i - 1]
    list.append(tempNum)

for i in range(0, len(list)):
    print(f"a{i + 1} = {list[i]}")
