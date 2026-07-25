# WAP to put even and odd elements of a list into two different lists.

li=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(li)
print(even)
print(odd)