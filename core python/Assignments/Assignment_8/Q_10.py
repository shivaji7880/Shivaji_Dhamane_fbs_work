# WAP to check given year is leap or not
# Function defination

def isLeap(year):
    if year%4==0:
        return 'Yes'
    else:
        return 'No'
y=int(input('Enter a year:'))  
res=isLeap(y)
print(res)