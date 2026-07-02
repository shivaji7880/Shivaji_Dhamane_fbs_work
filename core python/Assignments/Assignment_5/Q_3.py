# Taking input 

n=int(input('Enter number of passengers:'))
cost=int(input('Enter cost of per ticket:'))
print()
total_cost=0
for i in range(1,n+1):                                  # Number of passengers
    print(f'FOR PASSENGER {i}')
    age=int(input('Enter your age:'))
    print('-'*17)
    if age<12:                                         # Discount applied
        total_cost+=cost-(30/100*cost)
    elif age>59:
        total_cost+=cost-(50/100*cost)
    else:
        total_cost+=cost
print()        
print(f'Total amount for {n} tickets is {total_cost}rs.')   # Total paybill amount
        