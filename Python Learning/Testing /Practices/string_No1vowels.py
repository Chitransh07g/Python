s=input("Enter the string ")
s=s.lower()
l=len(s)
a=s.count("a")
e=s.count("e")   
i=s.count("i")   
o=s.count("o")   
u=s.count("u")
vowels=a+e+i+o+u
cons= l-vowels 
print(f"Number of vowels are :{vowels}")
print(f"Number of consonents are :{cons}") 