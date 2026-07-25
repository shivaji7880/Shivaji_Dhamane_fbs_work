# WAP to create a new list from existing list which contains cube of each element in list

li=[1,2,3,4,5,6,7,8,9]
size=len(li)
l2=[]
for i in range(size):
    l2.append(li[i]**3)   
print(l2)