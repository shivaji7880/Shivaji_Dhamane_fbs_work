# taking input
a=int(input('Enter area of one wall:'))
cost=int(input('Enter cost both interior and exterior wall:'))
#perform operation
t_area=a*7.5
actual_area=t_area-a/2
total_cost=a*cost

# Display result

print("Total cost",total_cost)