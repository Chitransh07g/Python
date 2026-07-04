outer = {}

print("\n================================================")
print("\t\tIts Input time 🖊️")
print("================================================")

number_of_classes = int(input("Enter the number of classes\n\t"))
for x in range(number_of_classes):
    class_name = input("Enter the name of the class\n\t")
    number_of_student = int(input(f"Enter the Number of Students in '{class_name}'\n\t"))
    inner = {}
    for y in range(number_of_student):
        student_name = input(f"Enter the name of the Student no {y+1}\n\t")
        marks = float(input(f"Enter the marks of '{student_name}' \n\t"))
        inner[student_name] = marks
    outer[class_name] = inner
    if number_of_classes > 1:
        print("\n------------------------------------------------\n")
        print("now For another class\n\n")

print("\n================================================")
print("\t\tIts OutPut Time 😃 ")
print("================================================")

for key in outer.keys():
    print(f"{key}")
    for skey in outer[key]:
        print(f"\t{skey} : {outer[key][skey]}")