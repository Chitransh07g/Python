string = "the quick brown fox jumps over the lazy dog"
replacer = string.replace('fox','cat')
title = replacer.title()
print(f"{title}\n{replacer.endswith('dog')}")