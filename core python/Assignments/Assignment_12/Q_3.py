# WAP to check given string is anagram or not.
s='abcdefghijklmnop'
s1=(input('Enter a string:'))
a=len(s)
b=len(s1)
c=0
for i in range(a):
    for j in range(a+1,a):
        if a==j:
            c+=1