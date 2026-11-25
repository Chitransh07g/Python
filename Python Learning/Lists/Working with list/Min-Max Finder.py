numbers = []

def min_max(numbers):

    if len(numbers) == 0:
        return None

    maxi = numbers[0]
    mini = numbers[0]

    for num in numbers:

        if num > maxi:
            maxi = num

        if num < mini:
            mini = num

    return (mini , maxi)

minimum , maximum = min_max(numbers)                 
print(f"The minimum number is {minimum} ")
print(f"The maximum number is {maximum} ")