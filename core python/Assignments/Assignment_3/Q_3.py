# Write a program to input angles of triangle and check wheather triangle is valid or not.
# Taking inputs

a=int(input('Enter measure of 1st angle:'))  
b=int(input('Enter measure of 2nd angle:'))
c=int(input('Enter measure of 3rd angle:'))

# Perform operation

sum=a+b+c

# display result

if sum==180:
    print('Valid triangle.')
    
else:
    print('Not valid triangle.')