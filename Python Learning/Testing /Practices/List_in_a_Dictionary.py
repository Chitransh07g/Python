pizza = {
    'crust' : 'thick' ,
    'toppings' : ['mushroom' , 'extra cheese']
}

# Summarise the order
print(f"You ordered a {pizza['crust']}-crust pizza With flowig toppings :")

for topping in pizza['toppings']:
    print(f"\t{topping}")