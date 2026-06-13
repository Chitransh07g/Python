rows = int(input("Enter the number of rows :- "))
a = [1]
b = [1 , 1]

if rows >= 1:
    print(a)
if rows >= 2:
    print(b)    

for x in range(rows - 2 ):
    a = [1]
    
    sum = 0
    for y in range(len(b) - 1):

        sum = b[y] + b[y+1]
        a.append(sum)
    a.append(1)
    print(a)
    b = a    