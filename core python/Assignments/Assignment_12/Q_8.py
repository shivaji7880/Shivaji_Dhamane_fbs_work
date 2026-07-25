# WAP to remove charactores from odd index values from the string.

s=input('Enter a string:')
s1=''
for i in range(len(s)):
    if i%2==0:
        s1+=s[i]       
print(s1)