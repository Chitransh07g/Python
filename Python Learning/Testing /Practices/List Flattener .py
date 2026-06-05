nested = [1, [2, 3], [4, [5, 6]], 7]
new = []

for num in nested:
    if isinstance(num,list):
        for x in num:
            if  isinstance(x,list):
               for y in x:
                   new.append(y)
            else:
               new.append(x)
    else :
        new.append(num)

print (new)                