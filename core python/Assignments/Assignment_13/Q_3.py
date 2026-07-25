#WAP to check a key is present in dictionary or not
dict={'id': '101', 'name': 'shivaji', 'sal': 32000, 'job': 'developer', 'address': 'pune'}
keys=dict.keys()

key=input('Enter key to check:')
if key in keys:
    print(f'{key} is present in dictionary.')
else:
    print(f'{key} is not present in dictionary.')
   