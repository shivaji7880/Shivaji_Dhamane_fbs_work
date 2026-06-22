# WAP to print sum of series upto n.
# Taking input

sum=0
n=int(input('How many numbers sum you wants:'))
for i in range(1,n+1):
    sum+=i
    
print(f'Sum of first {n} numbers is {sum}.')