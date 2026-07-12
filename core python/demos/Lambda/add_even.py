data=[1,2,3,4,5,6,7,8,9,10]
import functools
res=(functools.reduce(lambda x,y:x+y,filter(lambda x:x%2==0,data)))

#even=list(filter(lambda x:x%2==0,data))
#total=functools.reduce(lambda x,y:x+y,even)
print(res)
#print(total)
