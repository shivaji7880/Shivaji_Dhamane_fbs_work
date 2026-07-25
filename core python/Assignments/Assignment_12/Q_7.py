# WAP to calculate length of string without using library function.
s=input('Enter a string:')
li=list(s)
li.append(0)
length=li.index(0)
print('Length of string is',length)