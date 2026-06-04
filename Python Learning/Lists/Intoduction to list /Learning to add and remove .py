# learned about inserting ,,,, deleting or removing elements manually 
mottorcycle = ['honda','yamaha','suzuki']
print (mottorcycle)
# now modifying the list 
mottorcycle[0]= 'ducati'
print (mottorcycle)


# Adding the element to the  end of the list 
mottorcycle.append('BMW')
print (mottorcycle)

motorcycle = []
motorcycle.append('honda')
motorcycle.append('ducati')
motorcycle.append('bmw')
motorcycle.append('suzuki')
print(mottorcycle)


# inserting elements to the list at custom index
motorcycle.insert(0,'Duke')
print (motorcycle)


# deleting the element from the list ...... using del 
del motorcycle[1]
print (motorcycle)


# deleting the element from the list ...... using pop() method
#feature is that we can use it after we removed it ....
popped = motorcycle.pop()
print(popped)
print(motorcycle)


# we can also use index while popping out 
print (motorcycle.pop(2))


# using elemsnt name to remove from the list the same element 
mottorcycle.remove('ducati')
print (mottorcycle)
mottorcycle.pop(2)
print(mottorcycle)
