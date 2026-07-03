ages = {
    'Ayush': 17,
    'Areeba': 19,
    'Chitransh': 19
}

ages['Akash'] = 21
ages['Ayush'] = 16
del ages['Akash']
print(ages)

for name, age in ages.items():
    print(f"{name} is {age} years old")