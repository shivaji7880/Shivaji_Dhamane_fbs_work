# Write a python program to find elements in a given set that are not in another set.

s={1,2}
s2={1,2,3}
for i in s2:
    if i not in s:
        print(i)