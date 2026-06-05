string = input("Enter the String \n")
unique =[]

for ch in string:
    if ch not in unique : unique.append(ch)

print (f"The Unique Characters are :- {unique}")    