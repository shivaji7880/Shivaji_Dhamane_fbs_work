# Taking input

n=int(input('Enter number of terms you want:'))
sum=0
for i in range(1,n+1):
        sum+=n**i
print(sum)