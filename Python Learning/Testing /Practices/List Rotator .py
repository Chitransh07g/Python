numbers = [1, 2, 3, 4, 5]
num = int(input("Enter the times of rotation "))

if num <= len(numbers):
    for x in range(num):
       new = numbers.pop(0)
       numbers.append(new)

else :print("Out of range ")

print (f"The Rotated list is :-{numbers}")        