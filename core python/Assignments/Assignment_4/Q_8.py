# WAP to find which numbers are divisible by 7 and multiple of 5 in given range.
# Taking input

start=int(input('Enter starting:'))
end=int(input('Enter ending:'))

print('Following are the numbers which are divisible by 7 and multiple of 5.')
for i in range(start,end):
    d=i%10
    if i%7==0 and (d==0 or d==5):
        print(i)