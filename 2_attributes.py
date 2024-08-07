from helper import d
from colorama import Fore, Style
# Creating attributes for our classes

# What's an attribute?
#-- Attributes define the qualities of our objects and are stored in variables within a class

# There are two different types of attributes

#-- Class Attributes : attributes that are shared between all instances of a class
#-- Instance Attributes : Attributes that can vary between instances of a class

class Car():
    # Class attribute example
    wheels = 4

    def __init__(self, make, model):
        #instance attributes
        self.make = make
        self.model = model

# create a few instances of the car class
bugati = Car('Bugati', 'Veyron')
tesla = Car('Tesla', 'Model S')

print('BUGATI')
print(bugati.wheels)
print(bugati.model)

d()

print('TESLA')
print(tesla.wheels)
print(tesla.model)

d()

my_cars = list()
my_cars.append(bugati)
my_cars.append(tesla)
print(my_cars)

for car in my_cars:
    print(car.make)

d()

# Class Methods

#-- Methods define the actions or functionalities that our objects can perform

class Car():

    def __init__(self, make, model, mileage = 0): # __init__ method must always contain self as the first parameter
        self.make = make
        self.model = model
        self.mileage = mileage


tesla = Car('Tesla', 'Model S', mileage = 312)
# print(tesla.mileage)

class Character():

    def __init__(self, attk, lvl, hp= 100, mp= 25, deff=50):
        self.hp = hp
        self.mp = mp
        self.deff = deff
        self.attk = attk
        self.lvl = lvl

    def get_info(self):
        print(f'''
This character is level {self.lvl}
STATS:
HP --- {Fore.GREEN} {self.hp} {Style.RESET_ALL}
MP --- {self.mp}
DEF --- {self.deff}
ATTK --- {self.attk}''')
        
    def attack(self, target):
        target.hp -= 20

wizard = Character(20, 1, mp= 100)
warrior = Character(50, 1)
print(warrior.lvl)
warrior.lvl += 1
print(warrior.lvl)

d()
print("BATTLE")

wizard.get_info()
warrior.get_info()

print("Warrior is attacking wizard")
warrior.attack(wizard)

wizard.get_info()
warrior.get_info()
