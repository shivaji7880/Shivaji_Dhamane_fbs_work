# WAP to check given number is armstrong or not.

def noOfdigits(num):
    i=0
    while num>0:
        num//=10
        i+=1
    return i

def addition(num,digits):
    sum=0
    while num>0:
      d=num%10
      sum=sum+d**digits
      num//=10
    print (sum)

def isArmstrong(num,digits):
    if num==addition(num,digits):
        return True
    else:
        return False
      
num=int(input('Enter a number:'))
digits=noOfdigits(num)
res=isArmstrong(num,digits)
print(res)