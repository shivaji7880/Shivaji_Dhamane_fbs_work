s=input("Enter a string:")
li=[i for i in s.split(" ") if len(i)<5 ]
print(li)