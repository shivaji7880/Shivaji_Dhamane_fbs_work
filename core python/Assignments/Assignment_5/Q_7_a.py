#    A
# Taking input

n=int(input('Enter number of terms you want:'))
sum=0
while n>0:
    fact=1
    for i in range(1,n+1):
        fact*=i
    sum+=fact
    n-=1
print(sum)