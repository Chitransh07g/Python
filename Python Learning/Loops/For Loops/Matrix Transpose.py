def Inpmatrix():

    print("Enter the details of the first matrix")
    matrix01 = []
    for x in range(rows):
        row = []
        for y in range(cols):
            val = int(input(f"ENter [{x}] [{y}] :- "))
            row .append(val)
        matrix01.append(row)

    return matrix01

def transpose():
    matrix02 = []
    for x in range(cols):
        row = []
        for y in range(rows):
            val = a[y][x]
            row.append(val)
        matrix02.append(row)
    return matrix02    



rows = int(input("Enter the number of Rows :- "))
cols = int(input("Enter the number of Coloumns :- "))        

a = Inpmatrix()
b = transpose()
print(f"The Original Matrix is :- {a} \nThe Transpose of the Matrix is :- {b}")