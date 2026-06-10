i = 1
j = 1
n = int (input("Enter the diamond middle length\n"))
while i <= n:
    j = 1
    while j <= i:
        print("*",end = " ")
        j += 1
    i += 1
    print("")

k = n - 1
while k >= 1 :
    m = 1
    while m <= k:
        print("*", end = " ")
        m += 1
    k -= 1
    print() 

