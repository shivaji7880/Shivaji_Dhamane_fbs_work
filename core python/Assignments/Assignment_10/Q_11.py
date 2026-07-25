# WAP to print all numbers which are divisible by m and nin the list.

li=[]
for i in range(1,50):
    li.append(i)

n=int(input('Enter first number:'))   
m=int(input('Enter second number:'))
for i in li:
    if i%m==0 and i%n==0:
        print(i)