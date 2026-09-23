number = [1,4,5,6,3,5,7,4,6]

reversed_list = []

l = len(number)

for x in range(l - 1, -1, -1):
    reversed_list.append(number[x])

print(reversed_list)