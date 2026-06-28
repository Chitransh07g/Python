sentence = input("Enter a sentence\n")

# for Most frequent word:
words = sentence.split()
maximum = 0   
maximum_word = ""

for x in range (len(words)):
    count = 0
     
    for y in range(len(words)):
        if words[x] ==  words[y]:
            count += 1

    if count >  maximum:
        maximum_word = words[x]
        maximum = count 

print(f"Most frequent word: {maximum_word} \nFrequncy {maximum}")               

# Unique words 
unique = []
for x in words:
    if x not in unique:
        unique.append(x)
print(f"Unique words: {len(unique)}")

# Reversed 
new = words[::-1]
new_sentence = ""
for x in new:
    new_sentence +=   x + " "

print(f"Reversed :-{new_sentence.strip()}")  

# Palindrome (pehla word == aakhri word)
if words[0] == words[len(words)-1]:
    print("Palindrome :- Yes")
else :
    print("Palindrome :- No")    