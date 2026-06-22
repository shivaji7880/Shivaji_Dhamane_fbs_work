# WAP to print fibinacci series upto n.
# Taking input

a=-1
b=1
n=int(input('How many fibonacci numbers you want:'))
for i in range (n):
    c=a+b
    print(c)
    a,b=b,c