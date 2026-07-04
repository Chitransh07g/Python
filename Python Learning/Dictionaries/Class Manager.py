student_before = {}
student_after = {}
for x in range(4):
    name = input(f"Enter the name of the student {x+1} \n\t")
    marks = []
    print("Enter the marks of 3 subject one by one ")
    for y in range(3):
        a = int(input("\t"))
        marks.append(a)
    student_before[name] = marks    

maximum = 0 

for key in student_before.keys():
    name = key
    marks = student_before[key]
    average = sum(marks)/len(marks)
    student_after[name] = average
    if average >= maximum:
        maximum = average

print("Averge of every Student are ")

for key in student_after.keys():
    print(f"\t{key} : {student_after[key]}")

for key in student_after.keys():
    if student_after[key] == maximum :
        print(f"Student with maximum average \n\t{key} : {maximum}")