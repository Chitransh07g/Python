sent = input("\nEnter the sentence \n").split()
temp = {}

# this loop is for counting frequncy of all the words and storing it into a Dictionary

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

# It prints all the dict pair one by one 

n = 1 
for key in temp.keys():
    print(f"\t{n} → {key} : {temp[key]}")  
    n += 1

print("\n------------------------------------------------")
print("\nThe word / words with maximum Frequency  \n")

# Here ,  this finds the word or words with maxmimum frequency and displays it

maximum = max(temp.values())
ok = {}
for key in temp.keys():
    a = temp[key]
    b = key
    if a == maximum:
        ok[b] = a

n = 1
for key in ok.keys():
    print(f"\t{n} → {key} : {ok[key]}")
    n += 1

print("\n================================================")
print("\t \t Here it ends 😭")
print("================================================")