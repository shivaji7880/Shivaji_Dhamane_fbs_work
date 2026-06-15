# Write a program to enter P,T,R and calculate simple interest.
#Taking input 

p=int(input('Enter principle amount:'))
t=int(input('Enter time:'))
r=int(input('Enter rate of interest:'))

# Calculate simple interest

si=p*t*r/100

#Display result

print('Simple interest is',si)