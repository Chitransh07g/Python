n=int(input("Enter the number upto which you want to find "))
even=0
odd=0
for a in range(1,n+1):
    if a%2==0:
        even=even+a
    else :
        odd+=a
print("The sum of Even numbers are :",even)
print("The sum of odd numbers are :-",odd)        