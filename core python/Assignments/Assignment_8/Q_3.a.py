# Function definition
def result(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

# Taking input
n=int(input('Enter number of terms:'))

# Function calling
res=result(n)
print('Sum of series is',res)

        