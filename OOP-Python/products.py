class Product(object): 

    # status = 'for sale'

    def __init__(self, price, item_name, weight, brand, status='for sales'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        
    def sell(self):
        if self.status == 'sold':
            return self

    def returns(self, reason):
        if reason == 'defective':
            self.price = 0 
            self.status = 'defective'
            return self
        if reason == 'returned like new':
            self.status = 'for sale'
            return self
        elif reason == 'opened':
            self.status = 'used' 
            self.price = self.price * 0.8
            return self
    
    def tax(self, tax):
        # if status == 'sold':
        self.price *= tax
        return self.price

    def display_info(self):
        print('{} | {} | {}lbs | {} | {}').format(self.price, self.item_name, self.weight, self.brand, self.status)

product_iPhone = Product(300, 'iPhone', 5.5, 'Apple')
product_iPhone.tax(1.2)
product_iPhone.returns("opened")
product_iPhone.display_info()

product_tv = Product(1090, 'tv', 10, 'Samsung')
product_tv.tax(1.2)
product_tv.returns("defective")
product_tv.display_info()