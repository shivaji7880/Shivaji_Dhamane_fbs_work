# WAP to find maximum and minimum element from list

li=[6,3,8,9,2,5,7,0,1]
min=li[0]
max=li[0]
for i in range(1,len(li)):
    if li[i]<min:
        min=li[i]
for i in range(1,len(li)):
    if li[i]>max:
        max=li[i]
        
print(f'Maximum value is {max}')
print(f'Minimum value is {min}')