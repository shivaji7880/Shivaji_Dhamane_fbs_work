# Taking input
n=int(input('Enter total number of student:'))
total_per=0
for i in range(1,n+1):                                           # Number of students
    print(f'FOR STUDENT {i}')
    print()
    obt_marks=0
    for i in range(1,6):                                        # To take marks 
        mark=int(input(f'Enter marks of sub{i}:'))               
        obt_marks+=mark
    print()
    per=obt_marks/500*100                                       # Calculate percentage
    total_per+=per
    print(f'Percentage = {per}')
    print()
   
average_per=total_per/n                                        # Calculate average percentage
print(f'Average percentage = {average_per}')