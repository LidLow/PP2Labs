# Display numbers divisible by 5

def func(list):
    newList = [x for x in list if x % 5 == 0]
    return newList

answerList = func([10, 28, 74, 95])

for i in answerList:
    print(i)