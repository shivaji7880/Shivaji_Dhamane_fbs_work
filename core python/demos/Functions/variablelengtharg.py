def add(*num):   # Variable length argument
    sum=0
    for i in num:
        sum+=i
    return sum

res=add(2,4,6,8,5,8)
print(f'Addition is {res}.')
    