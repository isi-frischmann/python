class Animal(object):
    def __init__ (self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def animal_info(self):
        print 'Health: {}'.format(self.health)

Amy = Animal('Amy', 45) 
Amy.walk(), Amy.walk(), Amy.walk(), Amy.run(), Amy.run(),
Amy.animal_info()

class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)
    
    def pet(self):
        self.health += 5

luna = Dog("Luna", 20)
luna.walk(), luna.walk(), luna.walk(), luna.run(), luna.run(), luna.pet()
luna.animal_info()

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self
    
    def animal_info(self):
        super(Dragon, self).animal_info()
        print 'I am a Dragon'

fire = Dragon("Fire", 80)
fire.fly(), fire.animal_info()

charly = Animal('Charly', 70)
charly.fly(), charly.walk()
charly.animal_info()