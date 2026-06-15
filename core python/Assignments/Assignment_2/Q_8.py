# Swap two numbers using third variable
# Taking inputs

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))

print(f'''Numbers befor swapping
a={a}   b={b}''')

# Perform operation

c=a
a=b
b=c

# Display result

print(f'''Numbers after swapping
a={a}   b={b}''')
