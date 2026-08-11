class Product:
    def __init__(self,pid,pname,price,quantity):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantiy=quantity
    
    def showProduct(self):
        print(f'Pid:{self.pid}\tPname:{self.pname}\tPrice:{self.price}\tQuantity:{self.quantiy}')
        
    def __del__(self):
        print('Object is destroy...') 
    
p1=Product(732,'Watch',1299,3)
p2=Product(645,'Laptop',86999,2)
p3=Product(389,'NoteBook',79,4)
p1.showProduct()
p2.showProduct()
p3.showProduct()