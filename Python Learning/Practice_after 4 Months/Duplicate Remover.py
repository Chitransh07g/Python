numbers = [1,2,2,3,4,4,4,5]
unique = []

for x in range (len(numbers)):
    if numbers[x] not in unique :
        unique.append(numbers[x])

print("The original list -- ", numbers)
print("The Unique list -----", unique)