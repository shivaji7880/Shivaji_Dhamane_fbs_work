from S_Y import mod1 as M1
from T_Y import mod2 as M2
class Student:
    def __init__(self,rn,name,):
        self.roll=rn
        self.name=name
    M1.Symarks.getMarks()
    print()
    M2.Tymarks.tymarks()
    # print()
    def calPer(self):
        per=(M1.Symarks.setTotal()+M2.Tymarks.getTotal())/5
        return per
    def calGrade(self):
        if self.calPer()>=70:
            # Student.grade="A"
            return "A"
        elif self.calPer>=60:
            # Student.grade="B"
            return "B"
        elif self.calPer>=50:
            # Student.grade="C"
            return "C"
        elif self.calPer>=40:
            # Student.grade="Pass Class"
            return "Pass Class"
        else:
            # Student.grade="Fail"
            return "Fail"
   
        
    def __str__(self):
        return f"Roll:{self.roll}\nName:{self.name}\nPercentage:{self.calPer()}\nGrade:{self.calGrade()}"

s=Student(1,"Shivaji")
print(s)
print()
print("Successfully import packages and access values...")