# WAP to remve duplicates from list

li=[1,2,3,2,1,5,4,3,7,8,9]
l2=[]
for n in li:
    if n not in l2:
        l2.append(n)
print(l2)