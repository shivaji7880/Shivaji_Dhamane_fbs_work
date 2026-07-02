# WAP to print prime numbers between 1 to 100

for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)