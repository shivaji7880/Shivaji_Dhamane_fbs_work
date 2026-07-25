# WAP to revers the list

li=[1,2,3,4,5,6,7,8,9]
size=len(li)
li2=[]
for i in range(size-1,-1,-1):
    li2.append(li[i])
print(li2)