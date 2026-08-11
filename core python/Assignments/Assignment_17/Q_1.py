# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method

class Student:
    def __init__(self,studentid=100,name="ABC",age=20,percentage=70):
        self.studentid=studentid
        self.name=name
        self.age=age
        self.percentage=percentage
        
    def display(self):
        print(f'ID:{self.studentid}\nName:{self.name}\nAge:{self.age}\nPercentage:{self.percentage}')

    def accept(self):
        self.id=int(input("Enter student ID:"))
        self.name=input("Enter student name:")
        self.age=int(input("Enter student age:"))
        self.percentage=int(input("Enter student percentage:"))
    
    def calculateRank(self):
        if self.percentage>80:
           return "Outstanding"
        elif self.percentage>70:
            return "Distinction"
        elif self.percentage>60:
            return "First class"
        elif self.percentage>50:
            return "Second class"
        elif self.percentage>40:
            return "Pass"
        else:
            return "Fail"
            
    def __str__(self):
        return (f"""
                StudentID:{self.studentid}
                Name:{self.name}
                Age:{self.age}
                Percentage:{self.percentage}
                Rank:{self.calculateRank()}""")
    
s1=Student()
s1.display()
s1.accept()
print(s1)
