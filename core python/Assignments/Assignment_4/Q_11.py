# WAP to check given number is strong number.
# Taking input

num=int(input('Enter the number:'))
temp=num

sum=0
while num > 0:
    d=num%10
    fact=1
    while d>0:
        fact*=d
        d-=1
    sum+=fact
    num//=10
    
if temp==sum:
    print(f'{temp} is a strong number.')
else:
    print(f'{temp} is not a strong number.')
    