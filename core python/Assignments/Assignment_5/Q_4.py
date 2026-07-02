# Taking input
start=int(input('Enter starting value:'))
stop=int(input('Enter ending value:'))

for i in range(start,stop):
    sum=0
    n=i
    k=0
    while n>0:
        k+=1
        n//=10
        
    
    n=i
    while n>0:
        d=n%10
        sum+=d**k
        n//=10
        
    if sum==i:
        print(i)
        
        