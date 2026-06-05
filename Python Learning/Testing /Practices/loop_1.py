def new_func():
    i=1
    j=1
    for i<=5:
        for j<=5:
            if j%2==0 :
                print ("@", end="")
            else :
                print("$", end="")
            i++: j++
        
        print()

new_func()                   