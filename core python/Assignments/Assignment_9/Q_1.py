# WAP to print sum of factorials of n numbers using recursive function

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
    
def addition(num):
    if num==0:
        return 0
    else:
       return fact(num)+addition(num-1)
   
n=int(input('Enter n:'))
res=addition(n)
print(res)
        