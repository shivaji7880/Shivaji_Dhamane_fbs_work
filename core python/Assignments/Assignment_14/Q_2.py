# WAP to remove the intersection of second set with first set.

s={1,2,3,4,5,6,7,8,9}
s2={3,5,8,9}
a=(s.intersection(s2))
for i in a:
    s.remove(i)
print(s)