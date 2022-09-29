class Product:
    def __init__(self,productid:int,name:str,price:int,discount:int):
        self.productid=productid
        self.name=name
        self.price=price
        self.discount=discount
        
    def productdetails(self):
        return f"productid:{self.productid}\nname:{self.name}\nprice:{self.price}\ndiscount:{self.discount}"



def product():
    p1=Product(1,'p1',100,5)
    print(p1.productdetails())

#if __name__=='__main__':
   # product()