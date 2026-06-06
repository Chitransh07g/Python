count = 0
for ch in "Hello World":
    if ch.lower() in 'aeiou':
        count += 1
print(count)        


count = sum(ch.lower() in "aeiou" for ch in "Hello World")
print(count)