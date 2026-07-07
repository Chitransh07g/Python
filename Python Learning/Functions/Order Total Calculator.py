def  calculate_total(discount,*price):
    total = 0
    for x in price:
        total = total + x
    amount = total - discount
    return amount

print(calculate_total(10,100,200,50))
print(calculate_total(0,90))
print(calculate_total(5))