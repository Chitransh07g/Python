string = input("Enter the String\n")
new = ""

for i in string:
    c = 0
    if i not in new and i.isalpha():
        new += i 
        a = i
        for i in string:
            if a == i :
                c += 1
        print(f"{a} : {c}")
    a = ""