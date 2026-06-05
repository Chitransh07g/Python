
def additon():
    n=list(map(int,input("Enter the numbers to be addded separeted by ' , ' ").split(",")))
    print("The sum of the listed numbers  are :-", sum(n))
def substraction():
    s1=int(input("Enter the number to be subtracted "))
    s2=int(input("Enter the number from ehich the number to be sunbtracted  "))
    print("The subtraction of the number is :-",s2-s1)
def multiplication():
    m1=int(input("Enter the number for multiplication "))     
    m2=int(input("Enter the second number  for multiplication "))
    print("The multiplication of the numbers are ",m1*m2)
def division():
    d1=int(input("enter the Questionet "))       
    d2=int(input("Enter the divisor"))
    print("The division result is :-",d1/d2)

additon()
multiplication()  
substraction()
division()     