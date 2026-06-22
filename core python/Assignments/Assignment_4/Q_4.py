# WAP to print factorial of given number.
# Taking input


num=int(input('Enter the number:'))
temp=num
fact=1

while num>0:
    fact*=num
    num-=1
    
print(f'The factorial of {temp} is {fact}.')