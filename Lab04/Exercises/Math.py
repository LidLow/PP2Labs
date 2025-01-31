import math

#1. Write a Python program to convert degree to radian.
def degreesToRadians():
    degree = int(input("Degrees: "))
    radian = math.radians(degree)

    print("Radians:", round(radian, 6))


#2. Write a Python program to calculate the area of a trapezoid.
def areaOfTrapedzoid():
    height = int(input("Height: "))
    baseOne = int(input("First base: "))
    baseTwo = int(input("Second base: "))
    area = (baseOne + baseTwo) * height / 2

    print("Area of the trapedzoid:", round(area, 2))


#3. Write a Python program to calculate the area of regular polygon.
def areaOfPolygon():
    sides = int(input("Number of sides: "))
    length = int(input("Length of side: "))

    apothem = length / (2 * math.tan(math.pi / sides))
    area = apothem * length * sides / 2

    print("Area of the polygon:", round(area, 2))


#4. Write a Python program to calculate the area of a parallelogram.
def areaOfParallelogram():
    height = int(input("Height: "))
    length = int(input("Length: "))
    area = height * length

    print("Area of the parallelogram:", round(area, 2))


#Testing section