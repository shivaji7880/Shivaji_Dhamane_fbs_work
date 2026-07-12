for i in range(1,5):
    for j in range(1,13-i):
        print(' ',end=' ')
    for j in range(1,i*2):
        print('*',end=' ')
    print()
for i in range(1,5):
    for j in range(1,i):
        print(' ',end=' ')
    for j in range(24,i,-1):
        print('*',end=' ')
        
    print()