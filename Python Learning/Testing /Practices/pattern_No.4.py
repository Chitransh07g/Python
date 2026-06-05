n=5 
s=2
for i in range(1,n+1):
    for j in range(1,s):#for j in range (1,i+1)
        print(j,end="")
        
    print()
    s+=1#if use range (1,i+1)   you can remove this 
    # 1
    # 12
    # 123
    # 1234
    # 12345