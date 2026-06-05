words = ["python", "is", "awesome", "and", "fun"]
replace = []
count = len(words) -1

for dest in words[:]:
    replace.append(words[count])
    count -= 1

print (f"The reverse of the list is below \n{replace}")    