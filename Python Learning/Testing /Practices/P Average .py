marks = [int(x) for x in input("Enter the Marks Separated with spaces ").split()]

average = sum(marks) / len(marks)

if average >= 40 :print (" you passed the exam ")
else:print("You failed the exam ")