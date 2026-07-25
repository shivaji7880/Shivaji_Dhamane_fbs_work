# WAP to sort the list according to length of elements within the list.

li=[[1,2,3,4],[5,4,10],[23,54,7,2,9,3]]
for i in range(0,len(li)-1):
    if len(li[i])>len(li[i+1]):
        li[i],li[i+1]=li[i+1],li[i]
print(li)
