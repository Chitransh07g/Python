alien_1 = {'color' : 'green' , 'points' : 15}
alien_2 = {'color' : 'yellow' , 'points' : 10}
alien_3 = {'color' : 'red' , 'points' : 5}

#list of dictionaries 
aliens = [alien_1 , alien_2 , alien_3]

# make empty list for storing aliens 
for alien_number in range (30):
    new = {'color' : 'green' , 'points' : 5 , 'speed' : 'slow'} 
    aliens.append(new)  

for alien in aliens:
    print(alien)

# show the first five aliens 
print("First five aliens are ")
for alien in aliens[:5]:
    print(alien)
print("....")

# shows how many aliens have been created
print(f"The Total numbers od aliens :- {str(len(aliens))}")