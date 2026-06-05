import re

strin=input("Enter the String")
new=re.sub(r"[aeiouAEIOU]","",strin)
print(new)