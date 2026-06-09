num = int(input("Enter the number \n"))
n = 1

print("Lets go ")
while n <= num :

    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")

    elif  n % 3 == 0 :
        print("Fizz")

    elif n % 5 == 0 :
        print("Buzz")

    else :
        print(n)
    n += 1

print("Done ! ") 