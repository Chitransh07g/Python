touple = ()
offer = []
for _ in range(3):
    a = input("Enter name of the Player \n")
    b = int(input("Enter the Score of the player \n"))
    touple = (a,b)
    offer.append(touple)

for x in range(len(offer)):
    for y in range (len(offer)-1):
        a ,b = offer[y]
        c ,d = offer[y+1]
        if b < d :
            temp = offer[y]
            offer[y] = offer[y+1]
            offer[y+1] = temp 

name , score = offer[0]
print(f"Winner : {name.title()} ({score})")
name , score = offer[-1]
print(f"Last : {name.title()} ({score})")
print("Scoreboard :")

for x in range(len(offer)):
    name , score = offer[x]
    print(f"{x+1}. {name.title()} - {score}")