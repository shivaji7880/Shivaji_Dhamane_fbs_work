# Calculate compound interest taking P,R,T from user.
# Taking input

p=int(input('Enter principle amount:'))
r=int(input('Enter rate of interest:'))
t=int(input('Enter time:'))

# perform operation

ci=p*(1+r/100)**t-p

# Display result

print('Compound interest is',ci)