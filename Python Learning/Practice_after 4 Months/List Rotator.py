numbers = [1,2,3,4,5,6,7]
rotated = numbers.copy()


pos = int(input("Enter the postion of rotation - "))
indexs = 0

pos = pos % len(rotated)

for x in range(pos):
    element = rotated.pop(indexs)
    rotated.append(element)


print(rotated)