# Write a program to check if user has entered correct userid and password.
# Assining values

userid='abc6001'
password='Rohan_123'

# Taking input

u_id=input('Enter user id:')
pwd=input('Enter password:')

# perform operation

if (u_id==userid):
    if (pwd==password):
        print('Password match successfully!')
        
    else:
        print('Incorrect password.')
        
else:
    print('Incorrect userid.')