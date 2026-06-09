n = int (input("Enter the Number \n"))
x = 0

print("Here it starts ")
while x <= n:
    x += 1
    if x % 3 == 0 :
        continue
    print(x)    
print("Done!")