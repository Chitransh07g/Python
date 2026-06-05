#numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]
numbers = [9, 1, 2]

maximum = numbers[0]
second_maximum = float('-inf')

for num in numbers:
    if num > maximum :
        maximum = num 

for num in numbers:
    if num < maximum and num > second_maximum :
        second_maximum = num 

print (f"The Second largest number is :-{second_maximum}")