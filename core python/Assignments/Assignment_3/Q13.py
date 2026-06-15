
# Taking input

units=int(input('Enter electricity unit charges:'))

# Perform operation

b1=50*0.50
b2=100*0.75
b3=100*1.20

if units<=50:
    b=units*0.50
    
elif units<=150 and units>=51:
    b=b1+(units-50)*0.75
    
elif units<=250 and units>=151:
    b=b1+b2+(units-150)*1.20
    
elif units>250:
    b=b1+b2+b3+(units-250)*1.50
    
else:
    print('Invalid input.')
    
total_bill=b+(20/100*b)

print(f'Total electricity bill is {total_bill}rs.')