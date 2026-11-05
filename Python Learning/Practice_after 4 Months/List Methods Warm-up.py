numbers = [1,2,3,4,5]

numbers.append(6)
numbers.insert(2,7)
numbers.remove(5)   # isme sirf values kko dalke delete kr sakte h ... 
poped = numbers.pop()  # isme index dalte to index peka number ya element remove hota aur ... store hi kr sakte h .. 
print(poped)

print(numbers)
numbers.sort()
print(numbers)