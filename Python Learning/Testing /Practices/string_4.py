s = input("Enter the String ")
vowels = "aeiouAEIOU"
s1 = ""

for char in s:
    if char in vowels:
        s1 += "*"
    else:
        s1 += char

print(s1)
