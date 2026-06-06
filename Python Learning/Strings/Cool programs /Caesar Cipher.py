word = "hello"
char =""
for x in range(len(word)):
   char = char + chr(ord(word[x])+3)
   # here ord() gives the ASCII number of a character
   # chr() converts a number back to a character 
print(char)