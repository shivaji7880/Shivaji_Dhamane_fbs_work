# WAP to find all the anagram and group them together from a given list of strings.

words=['eat','tea','tan','ate','nat']

groups={}

for word in words:
    key=''.join(sorted(word))
    if key not in groups:
        groups[key]=[]
        
    groups[key].append(word)
    
print('Grouped anagrams:')
for group in groups.values():
    print(group)