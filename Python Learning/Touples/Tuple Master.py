student = ("Akash", "Rohit", "Ayush" , "Akash" ,"Rohan")
print(student[0])
print(student[-1])
print(student[1:4]) 

new = (95 , 'A')
a , b = new
print(a)
print(b)
print(student.count("Akash"))
print(student.index("Rohit"))

for i in student:
    if len(i) > 4:
        print(i)