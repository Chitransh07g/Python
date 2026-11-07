#numbers = [12, 45, 7, 45, 32, 8]
#numbers = [50, 10, 20, 30]
numbers = [5,5, 5]

maximum = float('-inf')
second = float('-inf')

s_place = -1
m_place = -1 

for x in range (len(numbers)):

    if numbers[x] > maximum :

        second = maximum
        s_place = m_place

        maximum = numbers[x]
        m_place = x
    

    elif numbers[x] < maximum and numbers[x] > second :
        second = numbers[x] 
        s_place = x 
       
print("Maximum:", maximum)
print("Maximum Index:", m_place)

if s_place == -1:
    print("Second Largest: Does not exist")
else:
    print("Second Largest:", second)
    print("Second Largest Index:", s_place)