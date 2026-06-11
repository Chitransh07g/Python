n = int(input("Enter the how many Numbers  You have to enter\n"))
sum = 0
print("Now Enter the number one by one")
store = []

for i in range(n):
    number = int(input(""))
    store.append(number)
    sum += store[i]

print(f"Sum :- {sum}")
print(f"Average :- {sum / n}")    