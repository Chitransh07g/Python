n = int(input("Enter how many numbers you have to enter "))
print("Enter the numbers one by one ")
numbers = []

for _ in range(n):
    numbers.append(int(input()))

larger = float('-inf')
second = float('-inf')

for x in range(n):
    if larger < numbers[x]:
        second = larger
        larger = numbers[x]
    elif second < numbers[x] < larger:
        second = numbers[x]
     
if second == float('-inf'):
    print("There is no second Largest Number")
else :    
    print(f"The second Largest Number is :- {second}")