# WAP to check given number is palindrom or not
# Function definition

def revers(num):
    temp=num
    rev=0
    while temp>0:
        d=temp%10
        temp//=10
        rev=rev*10+d
    return rev

def isPalindrom(num):
    if num==revers(num):
        return True
    else:
        return False
    
num=int(input('Enter number:'))
res=isPalindrom(num)
print(res)

    