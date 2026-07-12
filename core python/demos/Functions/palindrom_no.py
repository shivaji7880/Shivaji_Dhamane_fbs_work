def ispalindrom(num):
    temp=num
    rev=0
    while temp>0:
        d=temp%10
        temp//=10
        rev=rev*10+d
    if rev==num:
        return True
    else:
        return False
num=int(input('Enter number:'))
res=ispalindrom(num)
print(res)

    