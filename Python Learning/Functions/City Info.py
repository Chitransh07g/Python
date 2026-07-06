def describe_city(city,country='India'):
    output = city.title() + " is in " + country.title() +"."
    return output

a = describe_city('noida','america')
b = describe_city('noamundi')
c = describe_city(country='america',city='Noida')

print(f"{a}\n{b}\n{c}")