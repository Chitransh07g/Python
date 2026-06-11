base = int(input("Enter the Base number "))
exponent = int(input("Enter the exponential term "))
mul = 1
for i in range(exponent):
    mul *= base

print(f"{base} ^ {exponent} = {mul}")