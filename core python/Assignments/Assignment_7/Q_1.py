for i in range(1,6):
    for j in range(1,6):
        if i+j==6:
             print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(2,i+1):
        if i==j and i!=1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(2,6):
        if i+j==6:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()