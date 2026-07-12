# WAP to print sum of digits

def summation(num,sum=0):
    if num==0:
        return sum
    else:
        d=num%10
        return summation(num//10,sum+d)
    
n=int(input('Enter a number:'))
res=summation(n)
print(res)