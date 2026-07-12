# WAP to check given number is armstrong or not.

def digits(num):
    i=0
    while num>0:
        num//=10
        i+=1
    return i

def power(num):
    if num==1:
        return 1
    else:
        d=num%10
        return d**digit+power(num//10)
    
def isArmstrong(num):
    if num==power(num):
        return True
    else:
        return False
    
n=int(input('Enter a number:'))    
digit=digits(n)
res=isArmstrong(n)        
print(res)
        
        