n = int (input("Enter the number\n"))
a = 0
b = 1
c = 1
temp = 0

print("0 1", end = " ")
while c <= n-2:
    print(a+b, end = " ")
    temp = a +b 
    a = b
    b = temp
    c += 1
