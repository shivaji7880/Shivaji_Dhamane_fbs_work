# WAP to print revers of given number

def revers(num):
    rev=0
    while num>0:
        d=num%10
        num//=10
        rev=rev*10+d
    return rev

num=int(input('Enter a number:'))
res=revers(num)
print(res)