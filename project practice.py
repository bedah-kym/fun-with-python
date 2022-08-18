
class menu :
    def __init__(self,types,price, name,amount):
        self.types=types
        self.price=price
        self.name=name
        self.amount=amount
        
    #@property    
    def discount(self):
        new_price=0
        if self.price > 2000:
            new_price=self.price/10
            self.price=new_price
            
        else:
            raise Nameerror('invalid answer')
      


class school_books(menu):
    def __init__(self,types,price,name,amount,grade):
        super().__init__(types,price,name,amount)
        self.grade=grade
        
class stationery(menu):
    def __init__(self,types,price,name,amount,quality):
        super().__init__(types,price,name,amount)
        self.quality=quality
class novels(menu):
    def __init__(self,types,price,name,amount,author):
        super().__init__(types,price,name,amount)
        self.author=author
class papers (menu):
    def __init__(self,types,price,name,amount,use):
        super().__init__(types,price,name,amount)
        self.use=use

c_muturi=school_books('math revision',20000,'c muturi','200','high school')
c_muturi.discount()
print(c_muturi.grade)
print('you have a discount of',c_muturi.price,'kshs')




    
