# WAP to check given number is armstrong or not.

def noOfdigits(num):
    i=0
    while num>0:
        num//=10
        i+=1
    return i

def addition(num):
    sum=0
    digits=noOfdigits(num)
    while num>0:
      d=num%10
      sum=sum+d**digits
      num//=10
    return sum

def isArmstrong(num):
    if num==addition(num):
        return True
    else:
        return False
      
num=int(input('Enter a number:'))
res=isArmstrong(num)
print(res)
