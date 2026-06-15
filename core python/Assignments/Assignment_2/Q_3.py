# Convert distance given in feet and inches into meter and centemeter.
# Taking input

f=int(input('Enter distance in feets:'))
i=int(input('Enter distance in inches:'))

#perform operation
m=f*0.305
cm=m*100

m1=i*0.0254
cm1=m1*100
#Display result
print(f'''       Feets conversion                  Inches conversion
Meters:{m}  Centemeters:{cm}    Meters:{m1}  Centemeters:{cm1}''')




