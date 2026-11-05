numbers = [2,3,4,5,4,3]

# pehla number print krna h 
print(numbers[0])

# last number print krna h
print(numbers[-1])

print(len(numbers))

for x in range (len(numbers)):
    print(x,"-",numbers[x])

total = 0
for x in range (len(numbers)):
    total = total + numbers[x]

print("The sum of numbers are :-", total)
print("The average of the numbers are :- ", total/len(numbers))