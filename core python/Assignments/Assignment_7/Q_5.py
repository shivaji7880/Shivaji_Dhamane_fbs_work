for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,6):
        if j==1 and i!=5:
            print(j,end=' ')
        elif i==5:
            print(j,' ',end=' ')
        elif i==j:
            print(' '*j,i,end=' ')
        else:
            print(' ',end=' ')
    print()