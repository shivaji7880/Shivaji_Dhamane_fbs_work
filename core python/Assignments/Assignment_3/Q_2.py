# Write a program to input any alphabet and check wheather it is vowel or consonant.
# Taking input

alpha=input('Enter any alphabet:')

# Display result

if alpha in 'aeiouAEIOU':
    print(alpha,'is vowel.')
    
else:
    print(alpha,'is consonant.')