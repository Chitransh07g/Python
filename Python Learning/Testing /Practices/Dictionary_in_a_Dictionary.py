user = {
    'Chitransh' : {
        'first' : 'Chitransh' ,
        'middle' : 'Kumar' ,
        'last' : 'Gupta' ,
        'location' : 'Noamundi'
    },
    'Ayush' : {
        'first' : 'Ayush' , 
        'middle' : 'Kumar' ,
        'last' : 'Yadav' ,
        'location' : 'Noamundi'
    }
}

for username , user_info in user.items():
    print(f"\nUsername : {username}")
    print(f"\tFull name : {user_info['first'].title()} {user_info['middle'].title()} {user_info['last'].title()}")
    print(f"\tLocation : {user_info['location'].title()}")