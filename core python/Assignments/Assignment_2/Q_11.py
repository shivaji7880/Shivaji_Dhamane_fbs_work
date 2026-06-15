# Write a program to accept an integer amount from user and tell minimun number of notes needed for representing that amount.
# Taking input 

a=int(input('Enter amount:'))

temp=a

# Perform operation

n1=a//2000
a=a%2000
print('Number of 2000rs notes:',n1)

n2=a//1000
a=a%1000
print('Number of 1000rs notes:',n2)

n3=a//500
a=a%500
print('Number of 500rs notes:',n3)

n4=a//200
a=a%200
print('Number of 200rs notes:',n4)

n5=a//100
a=a%100
print('Number of 100rs notes:',n5)

n6=a//50
a=a%50
print('Number of 50rs notes:',n6)

n7=a//20
a=a%20
print('Number of 20rs notes:',n7)

n8=a//10
a=a%10
print('Number of 10rs notes:',n8)

print(f'Remaining amount is {a}rs.')

n=n1+n2+n3+n4+n5+n6+n7+n8

print(f'Minimum {n} notes required to represent {temp}rs.' )