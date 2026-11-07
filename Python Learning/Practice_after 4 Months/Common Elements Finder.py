number1 = [1, 3, 5, 7, 9, 3]
number2 = [3, 4, 5, 6, 3, 9]


common = []

for x in range (len(number1)):
    for y in range (len(number2)):
        if number1[x] == number2[y] and number1[x] not in common:
            common.append(number1[x])


print(f"The original lists are  : \n{number1} \n{number2}")
print(f"\nThe New list  is : {common}  \n Number of elements in the new list  are : {len(common)}")