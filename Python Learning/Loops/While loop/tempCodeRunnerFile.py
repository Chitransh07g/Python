number = int(input("Please guide me the number upto which you want to me to print Even numbers \n"))
x = 0
print ("All the even numbers are ")
while x <= number:
    if x % 2 == 0:
        print(x)
    x += 1

print("Done")