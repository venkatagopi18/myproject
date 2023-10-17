# calculator

class calculator():
    def __init__(self):
        self.result=0
    def display_result(self):
        print(self.result)
    def adding(self,number):
        self.result=self.result+number
    def substract(self,number):
        self.result=self.result-number
    def multiply(self,number):
        self.result =self.result*number
    def dividing (self,number):
        self.result =self.result/number

c=calculator()
c.adding(50)
c.substract(25)
c.multiply(2)
c.dividing(10)
c.display_result()

# shopping cart

class Cart():
    def __init__ (self):
        self.items = {}
        self.prices={}
    def display_items(self):
        print(self.items)
    def display_prices(self):
        print(self.prices)
    def add_items_prices(self,item,quantity,price):
        self.items[item]=quantity
        self.prices[item]=price
    def remove_items(self,item):
        del self.items[item]
        del self.prices[item]
    def get_total_price(self):
        self.total_price=0
        for item,quantity in self.items.items():
            self.total_price+=quantity*self.prices[item]
        print(self.total_price)

c=Cart()
c.add_items_prices("shirt",2,500)
c.add_items_prices("pant",1,1000)
c.add_items_prices("shoes",2,2000)
c.remove_items("shoes")
print(c.items)
print(c.prices)
c.get_total_price()

