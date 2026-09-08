try:
    num1=float(input("Enter a number:"))
    num2=float(input("Enter a number:"))
    
    opr=input("Enter an oprator to perform operation:")
    if opr=="_":
        print("Subtraction=",num1-num2)
    elif opr=="+":
        print("Addition=",num1+num2) 
    elif opr=="*":
        print("Multiplication=",num1*num2)
    elif opr=="/":
        print("Division=",num1/num2)
    else:
        raise Exception("You are using unsupported operator")
      
except ZeroDivisionError:
    print("Denomenator must be non zero number...")   
except ValueError:
    print("Must enter numeric value...")
except Exception as e:
    print(e)
else:
    print("Without exception run ho gaya beeeeee....")
finally:
    print("Bs bhai so jate hai abbbb")
