# WAP to remove the nth character from non empty string
n=input('Enter a string:')
i=int(input('Enter index from which you remove character:'))
new=n.replace(n[i],'')
print(new)