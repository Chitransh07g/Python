numbers = []
print ("Enter 8 numbers one by one ")

for _ in range(8):
    numbers.append(int(input()))

print (" The Even numbers among them are ...")

for num in numbers :
    if num % 2 == 0:
        print (num)