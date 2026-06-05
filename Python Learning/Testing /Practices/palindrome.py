s=input(" Enter the String ")
c=s.replace(" ","").lower()
r=c[::-1]

def check():
    if c==r:
        print("Palindrome")
    else:
        print("Not Palindrome")    

check()        