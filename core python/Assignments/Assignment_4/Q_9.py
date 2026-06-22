# WAP to print all numbers in a range divisible by given number.
# Taking input

start=int(input('Enter starting:'))
end=int(input('Enter ending:'))
num=int(input('Enter a number:'))

for i in range(start,end):
    if i%num==0:
        print(i)
