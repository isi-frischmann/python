class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0


    def displayInfo(self):
        print self.price
        print self.max_speed


    def ride(self):
        print 'Ridding {}'.format(self.miles * 10)
        return self

    def reverse(self):
        print 'Reversing'.format(self.miles-5)
        return self


bike1 = Bike(100, 25, 500)
print bike1.reverse


# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = True
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
#     def logout(self):
#         self.logged = False
#         print self.name + " is not logged in"
#         return self
#     def show(self):
#         print "My name is {}. You can email me at {}".format(self.name, self.email)
#         return self