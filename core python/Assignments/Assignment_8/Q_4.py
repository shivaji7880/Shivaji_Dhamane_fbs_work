# Function definition

def result(n):
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    return sum

# Taking input
n=int(input('Enter number of terms:'))

# Calling result Function
res=result(n)
print(f'Sum of all odd numbers from 1 to {n} is {res}.')