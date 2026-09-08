# You are developing an AI-based E-Commerce Recommendation System for an online
# store that sells products across multiple categories. The store wants a unified way to
# manage product information and stock levels while still being able to generate category-
# specific recommendations for customers browsing the site, all while keeping stock data
# safely encapsulated so it cannot be modified incorrectly from outside the class. Create a
# base class Product with a constructor that initializes protected attributes _name and
# _price, and a private attribute __stock representing the number of units available.
# Implement a public method update_stock(qty) that increases or decreases __stock by the
# given quantity, where qty may be positive for restocking or negative for a sale, while
# preventing the stock from going below zero, and a public method get_stock() that returns
# the current value of __stock, since it cannot be accessed directly from outside the class.
# Create three derived classes, Electronics, Clothing, and Groceries, each overriding a
# method recommend() to print a category-specific recommendation message referencing
# the product's _name and _price. Create a list containing a mix of Electronics, Clothing,
# and Groceries objects, loop through the list calling recommend() on each to demonstrate
# polymorphism, and then demonstrate a few calls to update_stock() and get_stock() to
# show that the stock levels are being managed safely through encapsulation. This task ties
# together inheritance, polymorphism, and encapsulation in a single integrated system,
# reflecting how these OOP principles work together in realistic AI-driven applications

class Product:
    def __init__(self,name,price,stock):
        self._name=name
        self._price=price
        self.__stock=stock
    def update_stock(self,qty):
        if self.__stock+qty>=0:
            self.__stock+=qty
        else:
            print("Stock cannot be negative!")
    def get_stock(self):
        return self.__stock
    def recommend(self):
        print("Product recommendation")

class Electronics(Product):
    def recommend(self):
        print("Tech recommendation:",self._name,"for",self._price)

class Clothing(Product):
    def recommend(self):
        print("Style recommendation:",self._name,"for",self._price)

class Groceries(Product):
    def recommend(self):
        print("Fresh recommendation:",self._name,"for",self._price)

products=[Electronics("Laptop",1200,10),Clothing("Jacket",80,15),Groceries("Apples",5,50)]

print("Recommendations")
for p in products:
    p.recommend()

print("\nStock Management")
p1=products[0]
print("Initial stock:",p1.get_stock())
p1.update_stock(5)
print("After restocking 5:",p1.get_stock())
p1.update_stock(-3)
print("After selling 3:",p1.get_stock())
p1.update_stock(-20)
print("Stock after invalid sale:",p1.get_stock())