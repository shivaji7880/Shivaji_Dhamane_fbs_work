# Write a program to check wheather a triangle is equalateral, isoscalen or scalen


s1=int(input('Enter side 1:'))
s2=int(input('Enter side 2:'))
s3=int(input('Enter side 3:'))

# Perform operation

if s1==s2==s3:
    print('Given triangle is equilateral.')
    
elif s1==s2 or s1==s3 or s2==s3:
    print('Given triangle is isoscales.')
    
else:
    print('Given triangle is scalene.')