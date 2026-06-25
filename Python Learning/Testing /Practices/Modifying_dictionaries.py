alien = {'color' : 'green'}
print(f"The alien is {alien['color']} .")

alien['color'] = 'red' #modified the value 
print(f"The alien is {alien['color']} .") 

x = 'slow'
alien1 = {'x_position' : 0 , 'y_position' : 25 , 'speed' : x}
print(f"Original postion {alien1['x_position']}")
if alien1['speed'] == 'slow':
    increment = 1
elif alien1['speed'] == "medium":
    increment = 2 
else :
    increment = 3

alien1['x_position'] = alien1['x_position'] + increment
print(f"New x_position {alien1['x_position']}")           