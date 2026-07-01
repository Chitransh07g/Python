launguage = {
    'jen' : 'python' ,
    'sarah' : 'c' ,
    'edward' : 'ruby' ,
    'phill' : 'python' 
}

friends = ['phill' , 'sarah']
for name in launguage.keys():
    print(name.title())

    if name in friends:
        print(f"Hi {name.title()} I see your favorite language is {launguage[name].title()} !")