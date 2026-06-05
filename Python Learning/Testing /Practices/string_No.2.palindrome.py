s= input("Enter the string ").lower().replace(" ","")
s1=s[::-1]
if s1==s:
    print ("The string is a palindrome String  ")
else :
    print("Not a palindrome string")    