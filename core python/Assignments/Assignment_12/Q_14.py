# WAP to count the number of occurances of each word in a string.
s=input('enter a string:')
words=s.split()

count={}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
        
for key in count:
    print(f'{key} : {count[key]}')