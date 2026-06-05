name = input("Enter your name ")
initials = ''

for ch in name.title():
    if ch.isupper():
        initials += ch+"."


print(f"The Initials of your Name is :-{initials.strip()}")        