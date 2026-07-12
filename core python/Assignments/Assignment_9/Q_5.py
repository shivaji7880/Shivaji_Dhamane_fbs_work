def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)
    
n=int(input('Enter number:'))
res=factorial(n)
print(res)