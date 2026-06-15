text = "   Hello World   "
new = text.strip()

print(f"After removing the spaces the string looks like :-{new} \nString in lower case :-{new.lower()} ")
print(f"Numbers of letter 'l' present int he string are :- {new.lower().count('l')}")