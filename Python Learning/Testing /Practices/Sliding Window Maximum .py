numbers = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
down = 0
up = k
counter = ((len(numbers)-k)+1)
maximum =[]
for x in range(counter) :
    window = numbers[down:up]
    maxi  = max(window)
    print(f"window {down+1} :- {window} --- maximum {maxi}")
    maximum.append(maxi)
    down += 1
    up += 1
    
print( f"The list of maximum numbers are below \n{maximum}")    