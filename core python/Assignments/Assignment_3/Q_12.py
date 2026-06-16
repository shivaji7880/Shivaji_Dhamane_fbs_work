# check given number is palindrom or not
# take input

num=int(input('Enter three digit number:'))
temp=num

# Perform operations

d1=temp%10
temp=temp//10

d2=temp%10
temp=temp//10

d3=temp%10
temp=temp//10

rev=d1*100+d2*10+d3

# Checking number Display result

if rev==num:
    print(f'{num} is palindrom number.')
    
else:
    print(f'{num} is not palindrom number.')

