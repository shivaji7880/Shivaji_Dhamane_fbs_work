for i in range(1,6):
      for j in range(1,6-i):
            print(' ',end=' ')
      for j in range(1,i+1):
               print(i+j-1,end=' ')
      for j in range(i-2,-1,-1):
           print(i+j,end=' ')
      print()