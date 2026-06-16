# Input 5 subject marks from user and display grade (eg.First class, Second class...)
# Taking inputs

m1=int(input('Enter 1st subject marks:'))
m2=int(input('Enter 2nd subject marks:'))
m3=int(input('Enter 3rd subject marks:'))
m4=int(input('Enter 4th subject marks:'))
m5=int(input('Enter 5th subject marks:'))

obtained_marks=m1+m2+m3+m4+m5

percentage=(obtained_marks/500)*100

print('Percentage:',percentage)

if percentage>=90:
    print('Outstanding')
    
elif percentage>=80:
    print('First class')
    
elif percentage>=70:
    print('Second class')
    
elif percentage>=60:
    print('Third class')
    
elif percentage>=40:
    print('Just passed')
    
else:
    print('Fail')
    
