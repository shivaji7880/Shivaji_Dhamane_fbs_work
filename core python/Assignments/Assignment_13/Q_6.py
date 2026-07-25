# python program to multiply all items in adictionary

d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
total=1
for i in d.values():
    total*=i
print(total)