# class CartItems:
#     def __init__(self,item:str,price:int,amount:int):
#         self.item  = item
#         self.price = price
#         self.amount = amount

# class Shop:
#     def __init__(self,)    def total(self):
#         return sum(self.price * self.item) for self in self.item

# cart_item1 = CartItems("eggs",250,4)
# cart_item1.total()

class CartItem:
    def __init__(self,name,price,quantity):
        self.name =  name
        self.price = price
        self.quantity = quantity
    def cart_item_total(self):
        return self.price * self.quantity

class Cart:
    def __init__(self,items:list[CartItem]):
        self.items = items
    
    def cart_total(self):
        return sum(item.cart_item_total)