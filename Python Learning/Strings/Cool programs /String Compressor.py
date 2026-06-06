strings = "aaabbbccddddee"
count = 1
new = ""
for x in range(1 , len(strings)):
    if strings[x]  == strings[x-1]:
        count += 1
    else :
        new += strings[x-1] + str(count)
        count = 1        
new += strings[-1] + str(count)
print(new)