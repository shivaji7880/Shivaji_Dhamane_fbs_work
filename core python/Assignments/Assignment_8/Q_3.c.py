# Function definition 
def power(num):
    return num**num

def result(n):
    sum=0
    for i in range(1,n+1):
        sum+=power(i)               # Calling power function 
    return sum

# Taking input
n=int(input('Enter number of terms:'))

# Calling result function
res=result(n)
print('Sum of series is',res)
