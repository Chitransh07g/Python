# list with some  numbers in it 

number = [1,2,3,4,5,6]

# printing first and last numbers from the list 

print("First elements = ",number[0])
print("Last element =  ",number[-1])

# printing the length of the list 

print("Length of the list = ",len(number))

# printing all the elements from the list 

print("Elements with their syntax")
a = 0 
for x in number:
    print(a,"-", x)
    a += 1

# finding the sum of all the elements from the list 

total = 0
for x in number :
    total += x
print("The Sum of all the elements in the list = ", total ) 

# finding average of the elements from the list 
avg = total / len(number)
print("Average of all the elements are ;- ", avg )