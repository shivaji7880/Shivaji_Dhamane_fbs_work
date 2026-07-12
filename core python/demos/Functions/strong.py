def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

    
def isstrong(num):
    temp=num
    sum=0
    while temp>0:
        d=temp%10
        temp=temp//10
        sum+=factorial(d)
    if num==sum:
        return True
    else:
        return False
num=int(input('Enetr num:'))
res=isstrong(num) 
print(res)