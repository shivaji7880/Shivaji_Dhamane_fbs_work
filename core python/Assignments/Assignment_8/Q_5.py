# Function definition

def prime(num):
    for i in range(2,num):
       if num%i==0:
         return 0

    return num
     
def result(n):
    sum=0
    for i in range(2,n+1):
        sum=sum+prime(i)
    return sum

# Taking input
n=int(input('Enter number of terms:'))

# Calling result Function
res=result(n)
print(f'Sum of all prime numbers from 1 to {n} is {res}.')