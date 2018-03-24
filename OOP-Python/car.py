# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: 
# price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. 
# Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. 
# In the class have a method called display_all() that returns all the information about the car as a string. 
# In your __init__(), call this display_all() method to display information about the car 
# once the attributes have been defined.


class Car(object):
    def __init__(self, price, speed, fuel, mileage): #You don't need to set the tax attribute here
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax()
        self.display_all()

    def tax(self):
        if self.price >= 10000:
            self.tax = 15
        else:
            self.tax = 12
        return self

    def display_all(self):
        print 'Price: {}'.format(self.price) 
        print 'Speed: {}mph'.format(self.speed) 
        print 'Fuel: {}'.format(self.fuel)
        print 'Mileage: {}mpg'.format(self.mileage)
        print 'Tax: {}%'.format(self.tax)
        print #You will have the two cars in a separate lists!! Otherwise the would be printed in one block. 

car_lucas = Car(25700, 70, 'Half', 0)
car_isi = Car(2000, 25, 'Empty', 400)
car_manuel = Car(10000, 25, 'Full', 550)
car_hannah = Car(7000, 36, 'Half Full', 100)