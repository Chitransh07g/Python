while True :
    password = input("Enter the password ")
    upper = False
    digit = False

    if len(password) > 8 :
        i = 0
        while i < len(password):
            char = password[i]
            if char.isupper():
                upper = True
            if char.isdigit():
                digit = True
            i += 1
        if upper == True and digit == True:
            print("Strong Password ")
            break 
        else :
            if not upper:
                print("Missed one uppercase letter")
            if not digit:
                 print("Missed one digit")
    else :
        print("Password must be more than 8 characters")             