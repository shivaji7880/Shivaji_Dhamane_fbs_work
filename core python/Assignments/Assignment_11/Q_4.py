# WAP to find second largest element in a list using bubble sort.

li=[12,43,65,78,98,56,45]
size=len(li)
for i in range(1,size):
    for j in range(0,size-i):
        if li[j]>li[j+1]:
             li[j],li[j+1]=li[j+1],li[j]
       
print(li)
print('Second largest element is:',li[-2])