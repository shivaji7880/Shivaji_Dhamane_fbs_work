# WAP to check given number is perfect or not.
# Taking input

num=int(input('Enter a numbner:'))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
        
if sum==num:
    print(f'{num} is a perfect number.')
else:
    print(f'{num} is not perfect number.')