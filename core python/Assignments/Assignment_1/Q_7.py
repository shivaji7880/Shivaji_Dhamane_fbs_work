# Program to find roots of quadratic equation 
# Taking input from user

a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
c=int(input('Enter value of c:'))

# Perform operation

d=b*b-4*a*c
r1=-b+d**0.5/2*a
r2=-b-d**0.5/2*a

# Display result
print(f'The roots of quadratic equation are {r1} and {r2}')