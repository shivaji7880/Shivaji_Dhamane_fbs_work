# WAP to calculate area of rectangle.
# Function definition

def area(length,breadth):
    return length*breadth

# Taking inputs
l=int(input('Enter length:'))
b=int(input('Enter breadth:'))

# Function calling
res=area(l,b)
print(f'Area of rectangle is {res} units.')
