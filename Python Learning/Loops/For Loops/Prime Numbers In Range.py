start = int(input("Enter the Starting Point\n"))
end = int(input("Enter the Ending Point\n"))

print(f"All the prime numbers between {start} and {end} are :- ")

for x in range(start , end+1):
    a = x 
    c = 0
    for i in range(1,x+1):
        if a % i == 0:
            c += 1
    if c == 2:
        print( a , end = " ")    
print()        