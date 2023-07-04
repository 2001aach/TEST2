# find the area of the square



def calculateArea(side):
    area = side * side
    return area

side = float(input("Enter the length of a side of the square: "))

area = calculateArea(side)

print("The area of the square is:", area)
0