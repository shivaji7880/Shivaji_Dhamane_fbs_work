def revers_num(num,rev=0):
    if num==0:
        return rev
    else:
        d=num%10
        return revers_num(num//10,rev*10+d)
n=int(input('Enter a number:')) 
res=revers_num(n)
print(res)