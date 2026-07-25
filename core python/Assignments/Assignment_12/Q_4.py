# WAP to form a new string where the first character and last character exchanged.
n=input('Enter a string:')
li=list(n)
li[0],li[len(li)-1]=li[len(li)-1],li[0]
for i in li:
    print(i,end='')

