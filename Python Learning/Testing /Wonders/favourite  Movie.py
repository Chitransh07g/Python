movies=[]
for value in range (0,5):
    movie = input("Enter the names of the movies no-" + str (value+1)+" ")
    movies.append(movie)
print (movies)     
# printint h fist and last name of the movie through indexing 
print("the name of the First movie is - "+movies[0])
print("the name of the Last movie is - "+movies[-1])