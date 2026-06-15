# Find sum of three digit number
# Take input from user

num=int(input('Enter three digit number:'))

#Perform operation

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

sum=d1+d2+d3

# Display result

print(f'Sum of three digits is {sum}')
