student = {
    'name' : 'Chitransh' ,
    'age' : 19 ,
    'grade' : 'A'
}
# printing only keys 
for key in student.keys():
    print(key)

# printing values only 
for value in student.values():
    print(value)

# Printing both    
for every in student.items():
    print(every)

# in cool format
for key in student.keys():
    print(f"{key} : {student[key]}")    