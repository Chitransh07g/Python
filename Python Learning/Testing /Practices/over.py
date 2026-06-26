# This method is when we know the number of inputs .... .
numbers = []
print ("Enter 8 numbers one by one ")
for _ in range (8):
    numbers.append(int(input()))

print("Even numbers in the list ")
for num in numbers:
    if num % 2 == 0:
        print (num )    

# This method when we donot  know the range ...

numbers = [int (x) for x in input(" Enter the numbers for which you want to find the even nubers \n Every numbers Should be Separates with Spaces ").split()]

print("Even numbers in the list ")
for num in numbers:
    if num % 2 == 0:
        print (num )
        
print("ALL done ")        
