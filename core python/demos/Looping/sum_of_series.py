# Write a program to print sum of first n numbers 

n=int(input('Enter value of n:'))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(f'Sum of first {n} numbers is {sum}.')