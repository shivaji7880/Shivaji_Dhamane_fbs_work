# WAP to check given number is prime or not.
# Taking input

num=int(input('Enter the number:'))
if num<=1:
    print(f'{num} is not prime nor composite number.')
else:
    for i in range(2,num//2):
      if num%i==0:
        print(f'{num} is not prime number.')
        break
    else:
        print(f'{num} is prime number.')