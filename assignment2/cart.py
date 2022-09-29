#import product
from product import *
class Cart:
    def __init__(self,quant:int,pr:int,ds:int):
      
        self.pr=pr
        self.quant=quant
        self.ds=ds

    def totalprice(self):
        return self.pr * self.quant - self.ds   



def cart(quant):
    #pr= product.price
    #ds=product.discount
    p1=Cart(100,quant,5)
    print("total amount:",p1.totalprice())
