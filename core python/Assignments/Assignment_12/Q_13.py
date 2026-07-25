# WAP to count number of digits and letters in a string
s=input('Enter a string:')
c=0
d=0
for i in s:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        c+=1
    else:
        pass
print(f'Number of characters:{c}')
print(f'Number of digits:{d}')