# n=input("Enter the number")
# c=n[::-1]
# if c==n:
#     print (n,"  Is a palindrome number")
# else :
#     print (n," Not a palindrome number")    

n=int(input("Enter the number "))
c=n

s=0
while n!=0:
    r=n%10
    n//=10
    s=(s*10)+r 
if s==c:
    print(c,"IS a palindrome number")
else :
    print(c,"Is not a palindrome number")    
      