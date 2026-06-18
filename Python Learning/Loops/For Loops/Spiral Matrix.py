def initialise():
    matrix = []
    for x in range (n):
        row = []
        for y in range (n):
            row.append(0)
        matrix.append(row)   
    return matrix 

def Spiral(b):
    a = b
    top = 0 
    left = 0 
    bottom = n-1 
    right = n-1 
    num = 1
    while top <= bottom and left <= right:
        for x in range (left , right+1):
            a[top][x] = num
            num += 1
        top += 1
        for x in range (top , bottom+1):
            a[x][bottom] = num
            num += 1
        right -= 1
        for x in range(right , left-1 , -1):
            a[bottom][x] = num 
            num += 1
        bottom -= 1          
        for x in range(bottom , top -1, -1 ):
            a[x][top] = num 
            num += 1
        left += 1

    return a
n = int(input("Enter the order of the Square Matrix...(just a number)  :-"))
b = initialise()
c = Spiral(b)

print(c)