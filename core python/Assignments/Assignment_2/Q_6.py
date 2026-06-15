# WAP to calculate total salary of employee based on basic ,da=10% of basic,ta=12% of basic,hra=15% of basic
# taking input

b_salary=int(input('Enter basic salary of employee:'))

# Perform operations

da=10*b_salary/100
ta=12*b_salary/100
hra=15*b_salary/100

total_salary=b_salary+da+ta+hra

# Display result

print('The employees total salary is',total_salary,'rs.')