# WAP to check if given number is armstrong or not.
# Taking inputs

# WAP to check given number is armstrong or not
# Taking input

num=int(input('Enter any number:'))
temp=num
i=0
while temp>0:
   temp//=10
   i+=1
   
temp=num  
sum=0
while num>0:
   d=num%10
   sum+=d**i
   num//=10

if temp==sum:
   print('Number is amstrong.')
else:
   print('Number is not amstrong.')
    
    
