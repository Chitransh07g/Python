my_list = [1 , 2 , 3 , 4 , 5]
print (my_list)

# Copying 
copy = my_list.copy()
print(copy)

# Adding  
c = [6]
my_list.append(6)# it only inserts the element to the end of the list 
my_list.insert(5,6) # it can insert any where just type the index ... it will add to it 
my_list.extend(c) # used for mainly attaching  multiple lists

print (my_list)

# Removing 
my_list.remove(6)#it removes the first 6 from the list 
removed = my_list.pop(4) # it removes and stores the removed number or element by passing its index number 
print(removed)
copy.clear()  # it removes everything 
print(copy)

print (my_list)

# Searching 
print(my_list.index(4)) # It just counts the index of the first element present 
print(my_list.count(6)) # it counts the number of occurrences of a value

# Ordering
my_list.sort()# For sorting in Asscendeing Order
print(my_list)  

my_list.sort(reverse=True)# For sorting in Descending Order
print (my_list)

my_list.reverse() # It  just reverses the list
print(my_list) 

