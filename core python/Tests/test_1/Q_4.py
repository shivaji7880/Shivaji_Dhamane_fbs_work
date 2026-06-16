# taking input
a=int(input('Enter area of one wall:'))
interior_cost=int(input('Enter interior cost:'))
exterior_cost=int(input('Enter exterior cost:'))
#perform operation
interior_area=8*a
exterior_area=7*a

total_cost=interior_area*interior_cost+exterior_area*exterior_cost

# Display result

print("Total cost",total_cost)
