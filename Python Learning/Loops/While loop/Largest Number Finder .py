largest = float('-inf')

while True :
    inp = input("Enter your input")
    if inp.strip() == "done":
        if largest == float('-inf'):
            print("No numbers entered!")
            break
        else :
            print(largest)
            break 
    elif float(inp) >= largest :
        largest = float(inp)
