# Write a program to input all sides of triangle and check wheather triangle is valid or not.
# Taking inputs

s1=int(input('Enter side 1:'))
s2=int(input('Enter side 2:'))
s3=int(input('Enter side 3:'))

# Perform operation

if (s1+s2)>s3 and (s1+s3)>s2 and (s3+s2)>s1:
    print('Valid triangle')
    
else:
    print('Invalid triangle')
