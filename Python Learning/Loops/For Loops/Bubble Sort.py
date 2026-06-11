n = int(input("Enter how many numbers you want to enter \n"))
print("Enter the numbers you want to add in the list")

numbers = []

for _ in range(n):
    numbers.append(int(input()))


for i in range(len(numbers)):
    for j in range(len(numbers)-1) :
        if numbers[j] > numbers [j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp 

print(f" Sorted BY Bubble Sort :- \n{numbers}")