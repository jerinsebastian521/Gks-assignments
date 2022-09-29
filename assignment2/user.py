import product as product,cart as cart
class User:
    def __init__(self,userid:int,name:str,address:str,email:str,phone:int):
        self.userid=userid
        self.name=name
        self.address=address
        self.email=email
        self.phone=phone

    
    def Details(self):
        return f"userid:{self.userid}\nname:{self.name}\naddress:{self.address}\nemail:{self.email}\nphone:{self.phone}"

    def update_details(self,name,address):
        self.name=name
        self.address=address

def user():
    p1=User(1,'jerin','kottayam','jerinseb521@gmail.com',807)
    print(p1.Details())
    print("----after updating----")
    p1.update_details('jerin','ernakulam')
    print(p1.Details())
    print("--PRODUCTS AVAILABLE--")

if __name__=='__main__':
    user()
    product.product()
    quant=int(input("enter quantity:"))
    cart.cart(quant)

   
   