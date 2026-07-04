sent = input("\nEnter the sentence \n").split()
temp = {}

for x in range(len(sent)):
    count = 0
    for y in range(x , len(sent)):
        if sent[x] == sent[y]:
            count += 1   
    if sent[x] not in temp :
        temp[sent[x]] = count 

print("\n================================================")
print("\t\tHere it starts 🖊️")
print("================================================")
print("\nHere are all the words with their Frequency\n")

for key in temp.keys():
    print(f"\t{key} : {temp[key]}")  

print("\n------------------------------------------------")
print("\nThe word / words with maximum Frequency  \n")

maximum = max(temp.values())
ok = {}
for key in temp.keys():
    a = temp[key]
    b = key
    if a == maximum:
        ok[b] = a

for key in ok.keys():
    print(f"\t{key} : {ok[key]}")

print("\n================================================")
print("\t \t Here it ends 😭")
print("================================================")