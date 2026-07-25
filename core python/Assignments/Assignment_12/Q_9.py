# WAP to calculate number of characters and words in a string.

s=input('Enter a string:')
a=s.split(' ')
print(f'Number of words in a string:{len(a)}')
c=0
for i in s:
    if i!=' ':
        c+=1
print(f'Number of characters in a string:{c}')