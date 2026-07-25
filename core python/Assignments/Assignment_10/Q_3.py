# WAP to find the second largest element
li=[23,45,76,88,34,87,90]
size=len(li)
for i in range(1,size):
    for j in range(0,size-i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(f'Second largest number is {li[-2]}')


        
