balance = 1000
while True:
    
    user = int(input("Enter the Number for your choice \n1. Deposit \n2. Withdraw \n3. Check Balance \n4. Exit\n")) 

    if user == 1:
        deposit = float(input("Enter the Amount of deposit\n"))
        balance += deposit
    elif user == 2:
        withdraw = float(input("Enter the Amount of Withdrawal\n"))
        if balance >= withdraw:
            balance = balance - withdraw
        else :
            print("Insufficient Balance!\n")
    elif user == 3 :
        print(f"Your remaining Balence is : {balance}\n")
    elif user == 4 :
        print("Thank you!\n")
        break
    else :
        print("Invalid Choice! Try Again \n")
