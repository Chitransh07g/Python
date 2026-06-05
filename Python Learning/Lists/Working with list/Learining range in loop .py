for value in range(1,5):
    print (value)

for value in range(1,6):
    print (value)
        
number = list(range(2,11))
print (number)

number = list(range(3,18,3))
print (number)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)    



squares=[value**2 for value in range (1,11)]
print (squares)