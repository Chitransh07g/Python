numbers = list(map(int ,input("Enter the numbers separed with spaces ").split(" ")))
new = []
# for removing duplicates 
for x in numbers:
    if x not in new:
        new.append(x)
# for sorting 
for y in range(len(new)):
    for x in range(len(new) -1 ):
        if new[x] > new[x+1]:
           temp = new[x+1]
           new[x+1] = new[x]
           new[x] = temp
print(f"The sorted list is :- {new}")
print(f"The smallest number in the list is :- {new[0]}")
print(f"The Largest number in the list is :- {new[len(new)-1]}")        