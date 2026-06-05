sentence = input("Enter the sentence ")
count = 0

for ch in sentence.lower():
    if ch in "aeiou":
        count += 1

print (f" In your sentence there are {count} Vowels ..")    