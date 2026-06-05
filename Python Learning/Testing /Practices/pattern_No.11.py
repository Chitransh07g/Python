#     *
#    * *
#   *   *
#  *     *
# *********
n=5
c=0
m=5
for a in range (1,n):
    for s in range (1,m):
        print(" ", end = "")
    for j in range (1,a+1):
       if j==1:
           print ("*",end="")   
       else:
           print (" ",end="")


    for k in range (c,0,-1) :
        if k==1:
           print("*",end="")
        else :
            print(" ",end ="")    
    c+=1
    m-=1
    print()  
for q in range (1,10):
    print("*", end ="")      