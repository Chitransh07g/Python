movies = []
print ("Enter the names of the  8 movies ")
for _ in range(8):
    mo = input()
    movies.append(mo)

print (movies)#


movies = [str(x) for x in input("Enter the names of the movies you like Sperated with Spaces\n").split()]
print (movies)