numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6, 5]
dupli = []

for num in numbers:
    if num not in dupli:
     dupli.append(num)

print (f"The list after removing  duplicates are :-{dupli} ")