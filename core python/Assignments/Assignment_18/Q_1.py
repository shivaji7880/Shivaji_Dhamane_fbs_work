class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        # print("Call me")
    def __add__(self):
        # num=self.real+self.imag
        # print(num)
        print(f"{self.real}+{self.imag}")
        
    def __sub__(self):
        # num=self.real-self.imag
        print(f"{self.real}-{self.imag}")
    def display(self):
        print(self.real+self)
    
    def __del__(self):
        print('Object is distoyed...')
        
c=ComplexNumber(10,"J")
c1=ComplexNumber(20,"i")
d=c+c1


        
