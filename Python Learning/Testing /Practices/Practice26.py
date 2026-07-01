launguage = {
    'jen' : 'python' ,
    'sarah' : 'c' ,
    'edward' : 'ruby' ,
    'phill' : 'python' 
}

print("The following languages have been mentioned ")
for lang in set(launguage.values()):
    print(lang.title())