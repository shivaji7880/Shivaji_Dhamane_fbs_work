# WAP to find longest common prefix of all strings.use the python set.

s=['flower','flow','flight']
prefix=''
shortest=min(s,key=len)
for i in range(len(shortest)):
    ch=shortest[i]
    if len(set(word[i] for word in s))==1:
        prefix+=ch
    else:
        break
    
print('Longest common prefix:',prefix)