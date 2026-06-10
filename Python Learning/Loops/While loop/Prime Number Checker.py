num = int(input("Enter the number "))
n = 1
c = 0
while n <= num :
    if num % n == 0:
        c += 1
    n += 1    

if c == 2:
    print(f"{num} is a Prime Number")
else :
    print(f"{num} is not a Prime Number")    