# Lecture Notes: Basics of OOP (Fundamentals)

## Creating Blueprints (Classes)
Object-Oriented Programming (OOP) revolves around the concept of "blueprints" (classes) that help us create multiple objects with similar attributes and behaviors. 

### Why Use OOP?
1. **Modularity**: OOP allows for better organization of code by breaking it down into (reusable) pieces (classes and objects).
2. **Reuse**: Once we build a class, we can reuse it to create multiple objects, reducing redundancy.
3. **Scalability**: Reusing code enables us to scale applications more efficiently.
4. **Maintenance**: OOP makes it easier to update specific instances of an object rather than modifying the entire catalog of data, or the entire codebase.

## Classes & Objects
- **Classes**: The blueprint that outlines the attributes and functionality of an object.
    - Look at `strings`, `dictionaries`, `lists`. These are all classes in python with their own methods and attributes
- **Objects**: Unique instances of a class, created based on the blueprint.

Basic Example:
```python

# We've been working with classes and objects this entire time!
str1 = str()
list1 = list()
dictionary1 = dict()

my_string = "This is a string data type. Each data type is its own class in Python. Each data type (class) has it's own operations (methods) we can use with it."
print(type(my_string))
print(type(list1))
print(type(dictionary1))

# Let's create a class of our own. 
# Python naming convention: Classes we make ourselves are always title case
class Car:
    pass

my_car = Car()
print(type(my_car))

```

## Attributes
**Attributes** define the qualities of our objects and are stored in variables within a class.

- **Class Attributes**: Attributes shared by every instance of the class.
- **Instance Attributes**: Attributes that may vary between different instances.

Example:
```python
class Car:
    # Class Attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance Attributes
        self.make = make
        self.model = model

# Creating instances of the Car class
car1 = Car('Toyota', 'Corolla')
car2 = Car('Honda', 'Civic')

print(car1.wheels)  # Output: 4
print(car1.make)    # Output: Toyota
print(car2.model)   # Output: Civic
```

## `init` Method
The `__init__` method is our class **constructor**, responsible for adding attributes to an object when creating a new instance of a class. This is what allows us to initialize individual instances of a class.

Example:
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car('Ford', 'Mustang')
print(car1.make)  # Output: Ford
```

## Methods
**Methods** define the actions or functionalities that our objects can perform. These include getting information, changing attributes, or incrementing values.

Example:
```python
class Car:
    def __init__(self, make, model, mileage=0):
        self.make = make
        self.model = model
        self.mileage = mileage

    # Method to get car info
    def get_info(self):
        return f'{self.make} {self.model}'

    # Method to drive the car
    def drive(self, miles):
        self.mileage += miles
        return f'Drove {miles} miles. Total mileage is now {self.mileage}.'

car1 = Car('Tesla', 'Model S')
print(car1.get_info())       # Output: Tesla Model S
print(car1.drive(100))       # Output: Drove 100 miles. Total mileage is now 100.
```

## Conclusion
OOP allows for creating well-structured, reusable, and maintainable code. By defining classes and objects, attributes, and methods, we can build complex applications with ease and clarity.