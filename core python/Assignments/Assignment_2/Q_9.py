# Swap two numbers without using third variable
# Taking inputs

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))

print(f'''Numbers befor swapping
a={a}   b={b}''')

# perform operation

a,b=b,a

# Display result

print(f'''Numbers after swapping
a={a}   b={b}''')
