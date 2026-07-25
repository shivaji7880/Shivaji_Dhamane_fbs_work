# WAP to create a duplicate of an existing list. It should not point to same list.

li=[1,2,3,4,5]
l2=[]
for i in li:
    l2.append(i)
print(li)
print(l2)
print(id(li))
print(id(l2))