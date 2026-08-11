class Book:
    
    count=0
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
    
    def showBook(self):
        print(f'Bid:{self.bid}\tBname:{self.bname}\t\tPrice:{self.price}\tAuthor:{self.author}')
        
    def __del__(self):
        print('Object is destroy...') 
    
b1=Book(1,'Wings of Fire',350,'A.P.J.Abdul kalam')
b2=Book(2,'The Alchemist',400,'Robert Coelho')
b3=Book(3,'Rich dad Poor dad',449,'Robert T.Kiy')
b1.showBook()
b2.showBook()
b3.showBook()
print(f'Total books:{Book.count}')