pin = 8989 
x = 0
while True:
    
    user = int(input("Enter the PIN\n"))
    if user == pin:
        print("Access Granted! Welcome.")
        break
    else :
        print("Wrong PIN! Try again.")
        x += 1  
    if x == 3:
        print("Card blocked!")
        break        