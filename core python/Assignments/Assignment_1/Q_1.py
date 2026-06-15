# Write a program to calculate the percentage of student based on mars of any 5 subjects.
# Taking input from user

sub1=int(input('Enter marks of 1st subject:'))
sub2=int(input('Enter marks of 2nd subject:'))
sub3=int(input('Enter marks of 3rd subject:'))
sub4=int(input('Enter marks of 4th subject:'))
sub5=int(input('Enter marks of 5th subject:'))

# perform operations total &  percentage

obt_M=sub1+sub2+sub3+sub4+sub5
per=obt_M/500*100

# Display result

print('Percentage is',per)


