# WAP to print first n prime numbers.
# Taking input

n=int(input('How many prime numbers you want:'))
num=2
while n>0:
    for i in range(2,num):
       if num%i==0:
           num+=1
           break
    else:
        print(num)
        num+=1
        n-=1