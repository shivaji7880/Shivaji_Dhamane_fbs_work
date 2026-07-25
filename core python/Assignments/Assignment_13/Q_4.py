# python program to genarate dictionary that contains numbers between 1 and n in the form (x,x*x)
dict={}
n=int(input('Enter the limit:'))
for i in range(1,n+1):
    dict[i]=i**2
    
print(dict)