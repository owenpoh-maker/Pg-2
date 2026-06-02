class Item:
    def __init__(self, name, quantity, price):
        self.name     = name
        self.quantity = quantity
        self.price    = price

# The function to calculate total price
def get_total(quantity, price):
    return round(quantity * price, 2)