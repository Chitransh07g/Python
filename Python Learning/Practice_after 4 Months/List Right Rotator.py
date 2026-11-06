numbers = [10, 20, 30, 40, 50]
rotated = numbers.copy()

pos = int(input("Enter the number of rotation :- "))

pos = pos % len(numbers)

for x in range (pos):
    element = rotated.pop(len(numbers)-1)
    rotated.insert(0,element)

print(f"The original list is :- {numbers}")
print(f"The rotated list is :- {rotated}")