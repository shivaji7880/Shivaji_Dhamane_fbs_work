# WAP to print fibonacci series using function.
# Function definition   
def fibo(n):
    a=1
    b=0
    for i in range(1,n+1):
        c=a+b
        print(c)
        a,b=b,c
# Taking input        
n=int(input('Enter number of terms you want:'))

# Calling function
fibo(n)