class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    
    def get_price(self, n):
        if n < 10:
            return self.price 
        elif 10 <= n <= 99:
            return self.price * 0.9
        else:
            return self.price * 0.8

    def make_purchase(self, m):
        if m <= self.amount:
            self.amount -= m
            return self.get_price(m)*m
        else:
            return "DONT HAVE THIS AMOUNT OF PRODUCTS"

a = [['apple', 200, 400], ['orange', 150, 350], ['watermelon', 50, 130]]

product = Product("apple", 200, 400)
print(product.make_purchase(20))