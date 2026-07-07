def multiply_all(*numbers):
    mul = 1
    if numbers == ():
        return mul
    elif numbers != ():
        for x in numbers:
            mul *= x
    return mul 

print(multiply_all(2,0,5))
print(multiply_all(1))
print(multiply_all())