# WAP to find all pair of elements in a list whose sum is equal to given number.

s={1,2,3,4,5,6,7,8,9}
s1=list(s)
n=int(input('Enter a number:'))
for i in range(len(s1)):
    for j in range(1,len(s1)-1):
        if s1[i]+s1[j]==n:
            print(s1[i],s1[j])