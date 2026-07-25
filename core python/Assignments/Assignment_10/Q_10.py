# WAP to remove all occurences of an elements from the list.

li=[1,2,3,4,5,6,7,8]
size=len(li)
for i in range(size):
    li.remove(li[0])
print(li)