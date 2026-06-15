# Write a program to input two angles from user and find third angle of the triangle.
# Taking input from user

a1=int(input('Enter measure of 1st angle:'))
a2=int(input('Enter measure of 2nd angle:'))

# perform operation

a3=180-(a1+a2)

# Display result

print('The measure of third angle of a triangle is',a3)
