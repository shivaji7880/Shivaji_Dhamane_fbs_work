# WAP to check wheather the number is prime or not.
def isPrime(num,i=2):
    if num==1:
        return False
    if i*i>num:
        return True
    if num%i==0:
        return False
    return isPrime(num,i+1)
n=int(input('Enter a number:'))    
if isPrime(n)==True:
    print(f'{n} is prime number.')
else:
    print(f'{n} is not prime number')
        