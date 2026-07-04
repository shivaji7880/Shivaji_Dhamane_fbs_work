# Function definition for calculating factorial
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

# Function defination for sum
def result(n):
    sum=0
    for i in range(1,n+1):
        sum+=factorial(i)
    return sum

# Taking input
n=int(input('Enter number of terms:'))

# Function calling
res=result(n)
print('Sum of series is',res)