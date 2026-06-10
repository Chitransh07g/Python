n = int(input("Enter your Input\n"))
x = n 
rev = 0

while x != 0:
    c = x % 10
    rev =  (rev*10) + c
    x = x // 10
    
if rev == n:
    print(f"{n} is a Palindrome")
else :
    print(f"{n} is not a Palindrome")