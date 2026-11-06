numbers = [4, 9, 2, 9, 7, 4, 1]

unique = []

minimum = numbers[0]
maximum = numbers[0]
ind = 0

for x in range (len(numbers)):
    if maximum < numbers[x] :
        maximum = numbers[x]
        ind = x

    if minimum > numbers[x]:
        minimum = numbers[x]   

    if numbers[x] not in  unique:
        unique.append(numbers[x])

no_of_unique = len(unique)    

print(f"The maximum number is : {maximum} ")
print(f"The minimum number is : {minimum} ")
print(f"The index of maximum number is :  {ind}")
print(f"Unique list : {unique} ")
print(f"Number of unique elements are : {no_of_unique}")