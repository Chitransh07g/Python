#1
#12
#123
#1234
#12345

n = 1
y = 1

while n <= 5:
    while y <= n:
        print(y,end="")
        y += 1
    y = 1
    print()    
    n += 1
    