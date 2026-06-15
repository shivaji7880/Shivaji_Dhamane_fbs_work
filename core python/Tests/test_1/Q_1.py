# taking input from user 

l=int(input('Enter length:'))
b=int(input('Enter breadth:'))
r=int(input('Enter radius:'))

cf=2*3.142*r
pm=b+2*l+(cf/2)

area=(l*b)+((3.142*r*r)/2)

#Display result

print('Area is',area)
print('perimeter is',pm)