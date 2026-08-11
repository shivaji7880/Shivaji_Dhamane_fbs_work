class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
    
    def showShirt(self):
        print(f'Sid:{self.sid}\tSname:{self.sname}\tType:{self.type}\tPrice:{self.price}\tSize:{self.size}')
        
    def __del__(self):
        print('Object is destroy...') 
    
s1=Shirt(101,'Oxford','Formal',799,'Small')
s2=Shirt(102,'Buttondown','Party wear',1199,'Large')

s1.showShirt()
s2.showShirt()
