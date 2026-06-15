# WAP to reverse three digit number
# Taking input

num=int(input('Enter any three digit number:'))

# Perform operation

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

# Display output

print(f'Reverse number is {d1}{d2}{d3}.')