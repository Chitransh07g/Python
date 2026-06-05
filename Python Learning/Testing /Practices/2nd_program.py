def addition():
    n = list(map(int, input("Enter the numbers to be added separated by ',' : ").split(",")))
    print("The sum of the listed numbers is:", sum(n))

def subtraction():
    s1 = int(input("Enter the number to subtract: "))
    s2 = int(input("Enter the number from which to subtract: "))
    print("The result of subtraction is:", s2 - s1)

def multiplication():
    m1 = int(input("Enter the first number for multiplication: "))
    m2 = int(input("Enter the second number for multiplication: "))
    print("The multiplication result is:", m1 * m2)

def division():
    d1 = int(input("Enter the dividend: "))
    d2 = int(input("Enter the divisor: "))
    if d2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("The division result is:", d1 / d2)

def minimum():
    n = list(map(int, input("Enter the numbers separated by ',' : ").split(",")))
    print("The minimum number is:", min(n))

def maximum():
    n = list(map(int, input("Enter the numbers separated by ',' : ").split(",")))
    print("The maximum number is:", max(n))

def ascending():
    n = list(map(int, input("Enter the numbers separated by ',' : ").split(",")))
    n.sort()
    print("The numbers in ascending order are:", n)

def descending():
    n = list(map(int, input("Enter the numbers separated by ',' : ").split(",")))
    n.sort(reverse=True)
    print("The numbers in descending order are:", n)

def calculate():
    print("Choose an operation: You just have to type the operation number alloted to them :- ")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Find Minimum")
    print("6: Find Maximum")
    print("7: Sort in Ascending Order")
    print("8: Sort in Descending Order")

    n = int(input("Enter your choice: "))

    if n == 1:
        addition()
    elif n == 2:
        subtraction()
    elif n == 3:
        multiplication()
    elif n == 4:
        division()
    elif n == 5:
        minimum()
    elif n == 6:
        maximum()
    elif n == 7:
        ascending()
    elif n == 8:
        descending()
    else:
        print("Invalid input")

calculate()
