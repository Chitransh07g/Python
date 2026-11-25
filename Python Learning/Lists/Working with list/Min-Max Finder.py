numbers = [5, -4, 9, 2, 7, -1]

def min_max(numbers):

    if len(numbers) == 0:
        mini = None
        maxi = None
        return (mini, maxi)

    maxi = numbers[0]
    mini = numbers[0]

    for num in numbers:

        if num > maxi:
            maxi = num

        if num < mini:
            mini = num

    return (mini, maxi)


minimum, maximum = min_max(numbers)

if minimum == None and maximum == None:
    print("The List is empty")

else:
    print(f"Max: {maximum}, Min: {minimum}")