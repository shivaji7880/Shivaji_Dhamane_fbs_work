data=[1,2,3,4,5,6,7,8,9,10]
from functools import reduce
def power(num):
    return num*num
#result=list(map(power,data))
res=reduce(lambda x,y:x+y,list(map(power,data)))
#print(result)
print(res)
