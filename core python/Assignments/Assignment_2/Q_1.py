# convert the time entered in hh,min and sec into seconds. 
# Taking input

h=int(input('Enter hours:'))
m=int(input('Enter minute:'))
s=int(input('Enter seconds:'))

# Perform operations

ss=h*3600+m*60+s

# Display result

print('Total seconds for given time are',ss)