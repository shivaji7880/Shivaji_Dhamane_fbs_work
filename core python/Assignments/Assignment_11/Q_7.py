# WAP to print intersection of two lists.

li=[1,2,34,5,6,8]
l2=[3,5,8,20,2]
size=len(li)
size2=len(l2)
union=[]
for i in range(0,size):
    for j in range(0,size2):
        if li[i]==l2[j]:
            union.append(li[i])
            
print(union)