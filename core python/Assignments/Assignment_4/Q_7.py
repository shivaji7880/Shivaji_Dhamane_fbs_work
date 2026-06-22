# WAP to print all integers upto n which aren't divisible by 2 and 3.
# Taking input

n=int(input('Enter last number:'))
for i in range(1,n+1):
    if i%2!=0 and i%3!=0:
        print(i)