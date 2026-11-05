numbers = [2,4,5,7,33,8,0,5,3]

length = len(numbers)
new = []

for x in range (length-1,-1,-1):
    new.append(numbers[x])

print("The original list --", numbers)
print("Reversed liist ---- ",new)    