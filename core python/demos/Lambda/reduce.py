data=[2,3,5,7,9,6,4,8]
import functools
res=functools.reduce(lambda x,y:x+y,data)
print(res)