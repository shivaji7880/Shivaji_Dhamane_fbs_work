# WAP to find sum of n numbers using recursion.

def summation(num):
    if num==0:
        return 0
    else:
        return num+summation(num-1)
n=int(input('Enter limit:'))   
res=summation(n)
print(res)