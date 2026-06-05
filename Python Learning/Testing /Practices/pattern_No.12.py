n = "computer"
l=len(n)
a=1
b=l-2
f=n[a]
ll=n[b]
print (n)
for a in range(1,l-1):
    f=n[a]
    ll=n[b]
    print(f,"    ",ll)
           
    a+=1
    b-=1
print(n[::-1])    