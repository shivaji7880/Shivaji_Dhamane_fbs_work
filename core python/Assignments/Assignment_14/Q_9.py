# WAP to find all the unique combinations of 3 numbers from a given list of numbers,adding up to target number.

numbers=[1,2,3,4,5,6]
target=10
res=set()
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if numbers[i]+numbers[j]+numbers[k]==target:
                res.add((numbers[i],numbers[j],numbers[k]))

print('Unique combinations:')
for i in res:
    print(i)