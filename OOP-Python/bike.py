# Assignment: Bike
# Create a new class called Bike with the following properties/attributes:

# price
# max_speed
# miles
# Create 3 instances of the Bike class.

# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

# Add the following functions to this class:

# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). 
# Have the second instance ride twice, reverse twice and have it displayInfo(). 
# Have the third instance reverse three times and displayInfo().

# What would you do to prevent the instance from having negative miles?

# Which methods can return self in order to allow chaining methods?

class Bike(object):
    def __init__(self, price, max_speed, miles = 0):  #creating class - values for the attribute have to be set here already
        self.price = price
        self.max_speed = max_speed
        self.miles = miles #miles = 0 above to set the miles for every attrubute automaticly to 0

    def displayInfo(self):
        print self.price, self.max_speed, self.miles

    def ride(self):
        print "Riding" 
        self.miles += 10   
        return self

    def reverse(self):
        print "Reverse"
        self.miles -= 5 
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(200, 50)
bike2 = Bike(570, 70)
bike3 = Bike(1070, 90)

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()