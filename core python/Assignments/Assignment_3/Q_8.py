# Write a program to check if user has entered correct userid and password. with matching captcha.
# Assining values

import random
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
    
    
captcha=random.randint(1000,9999)
print(captcha)
c=int(input('Enter captcha:'))

if c==captcha:
    print('Login succesfully.')
    
else:
    print('Login failed.')