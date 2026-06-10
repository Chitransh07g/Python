n = int(input("Enter your Input\n"))
total = 0

while n != 0:
    c = n % 10
    total += c
    n = n // 10

print(f"Sum of digits are : {total}")    
