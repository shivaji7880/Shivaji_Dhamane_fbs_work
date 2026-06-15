# WAP to calculate selling price of book based on cost price and discount
# Taking input 

cp=int(input('Enter cost price of book:'))
dis=int(input('Enter discount in percentage:'))

# Perform operation

sp=cp*(1+dis/100)

# Display output

print('Selling price of book is',sp)