n=5 
c=5
s=1
for i in range(1,n+1):
   if i==s:
    for j in range(1,c):
        print(" ",end="")
    for a in range (1,s+1):
       print(a,end="")
   s+=1
   c-=1
   print()
#     1
#    12
#   123
#  1234
# 12345