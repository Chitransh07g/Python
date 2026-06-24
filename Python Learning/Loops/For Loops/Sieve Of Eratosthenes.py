n = int(input("Enter the Limit "))

check  = [True] * (n+1)
check[0] = False
check[1] = False

for i in range (2 , n+1):
    if check[i] == True:
        for j in range(i*2 , n+1 , i):
           check[j] = False

for i in range(n+1):
    if check[i] == True:
        print( i , end = " ")

print()