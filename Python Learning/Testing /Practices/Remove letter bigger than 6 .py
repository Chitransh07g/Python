numbers = []

for num in range (10):
    numbers.append(num+1)

print (numbers)

for num in numbers[:]:
    #Read + modify karna hai saath mein → for num in numbers[:]
    if num > 6 :
      numbers.remove(num)

print (f"The numbers less than 6 are {numbers}")