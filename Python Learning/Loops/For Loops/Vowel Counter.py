word = input("Enter the String\n")
c = 0 
v = 0

for s in word:
    if s.lower() in "aeiou":
        v += 1
    else :
        c += 1

print(f"Total Vowels : {v}")            
print(f"Total Consonents : {c}")