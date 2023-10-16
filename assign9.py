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
    def _init_ (self):
        self.products = {}
        self.prices={}
    def display_products(self):
        print(self.products)
    def display_prices(self):
        print(self.prices)
    def add_products_prices(self,product,quantity,price):
        self.products[product]=quantity
        self.prices[product]=price
    def remove_products(self,product):
        del self.products[product]
        del self.prices[product]
    def get_total_price(self):
        self.total_price=0
        for item,quantity in self.products.items():
            self.total_price+=quantity*self.prices[item]
        print(self.total_price)

c=Cart()
c.add_products_prices("shirt",2,1000)
c.add_products_prices("shoes",1,5000)
c.add_products_prices("pant",2,2000)
c.remove_products("shoes")
print(c.products)
print(c.prices)
c.get_total_price()