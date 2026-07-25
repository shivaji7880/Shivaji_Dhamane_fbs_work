#WAP to take two strings and find larger string without using inbuilt fuction.

s=input('Enter 1st string:')
s1=input('Enter 2st string:')
c=0
c1=0
for i in s:
    c+=1
for i in s1:
    c1+=1
if c>c1:
    print('1st string is larger.')
else:    
    print('2st string is larger.')