li=[i for i in range(1,1000) if any(i%j==0 for j in range(2,10))]
print(li)

# for i in range(1,1000):
#     for j in range(2,10):
#         if i%j==0:
#             print(i)
#             break