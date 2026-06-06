strings = "The quick brown fox jumps over the lazy dog"
new = "" ; missing =[]
for n in "abcdefghijklmnopqrstuvwxyz":
    if n not in strings.lower():
        missing.append(n)
new += ", ".join(missing)
if new == "":print(f"Panagram ")
else : print(f"Not a Panagram \nMissing:-{new}")