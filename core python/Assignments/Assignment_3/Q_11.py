# Accept age of five peoples and ticket amount and then calculate total amount of tickets to travel for all of them based on following conditions:
# a.Chindren below 12 =30% discount
# b=Senior citizen (above 59)=50% discount
# Other need to pay full.

# Taking inputs

ticket_amount=int(input('Enter ticket amount:'))

p1=int(input('Enter your age (person 1):'))
p2=int(input('Enter your age (person 2):'))
p3=int(input('Enter your age (person 3):'))
p4=int(input('Enter your age (person 4):'))
p5=int(input('Enter your age (person 5):'))

# person 1
if p1<=12:
    amount=ticket_amount-(30/100*ticket_amount)
elif p1>=59:
    amount=ticket_amount-(50/100*ticket_amount)
else:
    amount=ticket_amount
    
# Person 2
if p2<=12:
    amount=ticket_amount-(30/100*ticket_amount)+amount
elif p2>=59:
    amount=ticket_amount-(50/100*ticket_amount)+amount
else:
    amount=ticket_amount+amount
    
# Person 3
if p3<=12:
    amount=ticket_amount-(30/100*ticket_amount)+amount
elif p3>=59:
    amount=ticket_amount-(50/100*ticket_amount)+amount
else:
    amount=ticket_amount+amount
    
# Person 4
if p4<=12:
    amount=ticket_amount-(30/100*ticket_amount)+amount
elif p4>=59:
    amount=ticket_amount-(50/100*ticket_amount)+amount
else:
    amount=ticket_amount+amount
    
# Person 5
if p5<=12:
    amount=ticket_amount-(30/100*ticket_amount)+amount
elif p5>=59:
    amount=ticket_amount-(50/100*ticket_amount)+amount
else:
    amount=ticket_amount+amount
    
    
print(f'Total amount of ticket is {amount}rs.')

    

    


 
