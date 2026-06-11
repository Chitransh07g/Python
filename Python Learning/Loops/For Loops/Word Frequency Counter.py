sentence = input("Enter the sentence ")
new = sentence.lower().split(" ")
spare = []
for i in new:
    
    c = 0
    if i not in spare :
        spare.append(i)
        for j in new:
            if j == i :
                c += 1 
        print(f"{i} : {c}")    
       