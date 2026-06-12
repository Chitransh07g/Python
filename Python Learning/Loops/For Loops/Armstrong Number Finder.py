#  What is an Armstrong Number?
#  
#  A number where sum of each digit raised to power of total digits = number itself
#  Example:153 → digits: 1, 5, 3 → total digits: 3
#                        1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✅ Armstrong!
#                        
#                        123 → 1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ❌ Not Armstrong

start = int(input("Enter the starting point :-"))
end = (int(input("Enter the ending point :- ")) )
counter = 0

print(f"ALL the Armstrong number from {start} to {end} are :-")
for q in range ( start , end + 1 ):
    total = 0 
    word = str(q)

    for x in word:
        power = 1
        a = int(x)

        for y in range(len(word)):
            power *= a

        total += power    
    if total == q :
        print(f"{q} is a Armstrong Number") 
        counter += 1
if counter == 0 :
    print("NO Armstrong Number in this range ") 