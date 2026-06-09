
while True :
    line = input("Enter the input\n")
    if line == "":
        print( "Input cannot be empty! Try again.")
        continue
    elif line.strip() == "":
        print("Input cannot be only spaces! Try again.")
        continue
    else :
        print(f"Valid input: {line}")
        break
    