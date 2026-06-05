#     1
#    121
#   12312
#  1234123
# 123451234
n=5 
c=5
s=1
for i in range(1,n+1):
   if i==s:
    for j in range(1,c):
        print(" ",end="")
    for a in range (1,s+1):
       print(a,end="")
    for b in range  (1,s):
       print(b,end="") 
   s+=1
   c-=1
   print()