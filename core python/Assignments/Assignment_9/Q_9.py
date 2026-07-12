# WAP to calculate m to the power n

def powers(num,power):
    if power==1:
        return num
    else:
        return num*powers(num,(power-1))
    
num=int(input('Enter number:'))
power=int(input('Enter power:'))
res=powers(num,power)
print(res)