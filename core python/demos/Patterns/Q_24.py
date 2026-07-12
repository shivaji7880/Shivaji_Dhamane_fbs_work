for i in range(1,5):
    for j in range(1,5):
        if i==1:
            print(j,end=' ')
        elif i==2:
            print(chr(64+j),end=' ')
        elif i==3:
            print(6+j,end=' ')
        else:
            print(chr(68+j),end=' ')
            
    print()
            