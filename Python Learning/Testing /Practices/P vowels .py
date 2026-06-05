sentence = input("Enter the  Sentence \n")
vowels = 0 
conso = 0 

for ch in sentence.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            conso += 1

print (f"Numbers od Vowels are :- {vowels}")
print(f"Numebrs od consonents are :- {conso}")   