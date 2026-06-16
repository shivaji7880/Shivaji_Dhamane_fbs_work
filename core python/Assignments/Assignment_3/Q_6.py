# calculate profit and loss

# Taking input

cp=int(input('Enter cost price:'))
sp=int(input('Enter selling price:'))

# perform operation

amount=sp-cp

# profit

if amount>0:
    print(amount,'is the profit')
    
# no loss no profit  
 
elif amount==0:
    print('No loss no Profit.')
    
# loss  
  
else:
    print(amount,'is the loss')