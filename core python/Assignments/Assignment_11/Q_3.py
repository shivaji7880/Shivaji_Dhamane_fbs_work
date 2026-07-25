# WAP to sort the list according to second element in sublist.

li=[[1,4],[2,5],[5,3],[8,5]]
li.sort(key=lambda x:x[1])
print(li)