#marks = list(map(int , input("Enter the marks separated with gaps ").split(' ')))

marks = [int(x) for x in input("Enter marks separated by spaces: ").split()]
average = sum(marks) / len(marks)

if average >= 40:
    print("You passed!")
else:
    print("You failed.")  