# WAP to check given number is present in list or not.Aslo check how many time number is appeared

li=[1,2,3,4,5,2,9,5,6,7,8,2,1,9,6]
num=int(input('Enter a number:'))
c=0
s=len(li)
for i in li:
    if num==i:
        c+=1
if c==0:           
    print(f'{num} is not in list.')
else:
    print(f'{num} is present {c} times in a list.')
    
