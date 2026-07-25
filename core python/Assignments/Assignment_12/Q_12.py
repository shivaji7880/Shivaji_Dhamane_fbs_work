# WAP to calculate number of lowecase characters in a string.

s=input('Enter a string:')
c=0
for i in s:
    if i.islower():
        c+=1
print(f'Number of lower case characters are:{c}')