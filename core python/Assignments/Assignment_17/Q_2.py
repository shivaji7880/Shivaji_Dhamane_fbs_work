# Create a derived class from Student as EnggStudent with:
# a. data members :
# i. branch
# ii.internalmark

# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

class Student:
    def __init__(self,studentid=100,name="ABC",age=20,percentage=70):
        self.studentid=studentid
        self.name=name
        self.age=age
        self.percentage=percentage
        
    def display(self):
        print(f'ID:{self.studentid}\tName:{self.name}\tAge:{self.age}\tPercentage:{self.percentage}')

    def Accept(self):
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
    
class EnggStudent(Student):
    def __init__(self, studentid=100,name="ABC",age=20,percentage=70,branch="Electronic",internalmark=80):
        super().__init__(studentid,name,age,percentage)
        self.branch=branch
        self.internalmark=internalmark
    
    def display(self):
        print(f'Branch:{self.branch}\tinternal:{self.internalmark}\t',end=' ')
        return super().display()
    
    def accept(self):
        self.id=int(input("Enter student ID:"))
        self.name=input("Enter student name:")
        self.age=int(input("Enter student age:"))
        self.percentage=int(input("Enter student percentage:"))
        self.branch=(input("Enter student branch:"))
        self.internalmark=int(input("Enter student internal marks:"))
    
    def calculateRank(self):
        return super().calculateRank()
       
    def __str__(self):
        return super().__str__()+f"""
                Branch:{self.branch}
                Internal_marks:{self.internalmark}"""
           
s1=Student(12,'Shiva',21,87.90)
s1.display()
print()
e1=EnggStudent()
e1.display()
print()
e1.accept()
e1.calculateRank()
print(e1)