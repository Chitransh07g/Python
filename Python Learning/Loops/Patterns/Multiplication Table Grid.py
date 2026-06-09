# 1       2       3       4       5
# 2       4       6       8       10
# 3       6       9       12      15
# 4       8       12      16      20
# 5       10      15      20      25


i = 1 
j = 1 


while i <= 5:
    while j <= 5:
        print(i * j , end="\t")
        j += 1
    j = 1    
    i += 1
    print()   