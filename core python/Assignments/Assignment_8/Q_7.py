# WAP to print sum of digits in given number
# Function defination

def digit(num,sum):
    if num>0:
     sum+=num%10
     num=num//10
     sum=digit(num,sum)
    return sum

# Taking input
n=int(input('Enter any number:'))

# Calling function 
res=digit(n,0)
print(res)
