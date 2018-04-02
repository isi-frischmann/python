class Store (object):

    def __init__(self, products, address, owner):
        self.products = products
        self.address = address
        self.owner = owner

    def add_product(self, product):
        # if item not in products:
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
    
    def total_amount(self):
        return len(self.products)
    
    def product_amount(self, name):
        count = 0
        for item in self.products:
            if name in item:
                count += 1
        return count
    
    def inventory(self):
        productItems = ''
        for item in self.products:
            productItems += item + ', '
        return productItems

zankerRoad = Store(['iPhone smartphone', 'Samsung smartphone', 'coffee'], '1920 Zanker Road', "Mrs. Schmid")
zankerRoad.add_product('honey')
zankerRoad.add_product('MBP')
print(zankerRoad.inventory())
print(zankerRoad.product_amount('iPhone'))
# print('next product\n')
# middlefield = Store(['iPhone', 'Laptop'], '525 Middlefield Road', "Mrs. Frischmann")
# middlefield.inventory()
# middlefield.remove_product('Laptop')
# middlefield.inventory()
