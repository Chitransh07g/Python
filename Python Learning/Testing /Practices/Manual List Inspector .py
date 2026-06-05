numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]
addition = 0
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    addition = addition + num 

    if num > maximum:
        maximum = num 

    if num < minimum:
        minimum = num 

print (f"The sum of the list is :- {addition}")
print (f"The maximum number among the list is :- {maximum}")
print (f"The minimum number among the list is :- {minimum}")