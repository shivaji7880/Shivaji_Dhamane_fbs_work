# WAP to count the frequency of words appearing in a string using a dictionary
s=input('Enter a string:')
a=s.split(' ')
d={}
for i in range(len(a)):
    n=a.count(a[i])
    d[a[i]]=n
print(d)