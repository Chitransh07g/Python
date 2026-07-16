def calculate_grade(student_name,*scores):
    length  = len(scores)
    total = 0
    
    if length > 0 :
        for x in scores:
            total = total + x 
        average = total / length 
        if average >= 90:
            grade = "A"
        elif average < 90 and average >= 75:
            grade = "B"
        elif average < 75 and average >= 50 :
            grade = "C"
        else :
            grade = "D"
        output = student_name.title() + "\n\t Average = " + str(average) +"\n\t Grade = "+ grade

    else :
        output = student_name.title() + "\n\tNo scores Provided"      
    return output

print(calculate_grade("Chitransh",65,98,75,52)) 
print(calculate_grade("chitransh"))
print(calculate_grade('Chitransh',1))