# WAP to find unique words and theire frequency. Use python set

s=input('Enter a string:')
words=s.split()
unique=set(words)
for word in sorted(unique):
    print(word,':',words.count(word))