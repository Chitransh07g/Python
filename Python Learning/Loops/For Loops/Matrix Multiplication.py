def matrix1(rows1 , col1):
    print("Enter the deatils for First matrix")
    matrix01 = []
    for x in range(rows1):
        row = []
        for y in range(col1):
            val = int(input(f"Enter [{x}][{y}] :- "))
            row.append(val)
        matrix01.append(row)
    return matrix01    
    
def matrix2(rows2 , col2):
    print("Enter the deatils for Second matrix")
    matrix02 = []
    for x in range(rows2):
        row = []
        for y in range(col2):
            val = int(input(f"Enter [{x}][{y}] :- "))
            row.append(val)
        matrix02.append(row)
    return matrix02    
        
rows1 = int(input("Enter the Rows of First matrix :- "))
col1 = int(input("Enter the Coloumn of First matrix :- "))
a = matrix1(rows1 , col1)

rows2 = int(input("Enter the Rows of Second matrix :- "))
col2 = int(input("Enter the Coloumn of Second matrix :- "))
b = matrix2(rows2 , col2)

new = []
if col1 == rows2 :

    for x in range (rows1):
        row = []
        for y in range(col2):
            total = 0
            for k in range(col1):
                total += a[x][k] * b[k][y]
            row.append(total)
        new.append(row)
    print(new)
else : 
    print("Matrix Multiplication not possible")    