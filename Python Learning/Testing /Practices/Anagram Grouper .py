words = ["eat", "tea", "tan", "ate", "nat", "bat" , "abt"]
groups = []

for word in words:
    for group in groups:
        if sorted(group[0]) == sorted(word):
            group.append(word)
            break
    else:
        groups.append([word])

print(groups)
