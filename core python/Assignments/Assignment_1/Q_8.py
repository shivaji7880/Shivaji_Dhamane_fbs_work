# Write a program to convert days into years ,weeks snd days.
# Taking input 

days=int(input('Enter number of days:'))

# Calculate years

years=days//365
days=days%365

# Calculate weeks

weeks=days//7
days=days%7

# Display result

print(f'Years:{years}, Weeks:{weeks}, Days:{days}.')
