matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

group = []

for col in range(3):
    cool = []
    r = 2
    for row in range (2, -1, -1):
        cool.append(matrix[r][col])
        r -= 1
    group.append(cool)


for row in group:
    print(row)