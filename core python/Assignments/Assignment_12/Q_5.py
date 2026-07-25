# WAP to count number of vowels in a string

s=input('Enter a string:')
c=0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        c+=1
print(c)