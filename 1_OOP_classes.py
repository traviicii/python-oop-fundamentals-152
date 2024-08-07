from helper import d
# Object Oriented Programming and Classes

# OOP: a concept revolving around 'blueprints' (classes) that help us to create multiple objects with similar attributes and behaviors

# why use this OOP concept?

#-- Modularity : OOP allows for better organization of code by breaking it down into (reusable) pieaces (classes and objects)
#-- Reusability : Once we build a class, we can reuse it to create multiple objects, reducing redundancy
#--Scalability : Reusing code allows us to scale our applications with more efficiency
#-- Maintenance : OOP makes it easier to update specific instances of an object rather than modifying an entire database, or an entire code base

# What are classes and objects??

#-- Classes : Classes are the blueprint that outlines the attributes and functionality of an object
#-- Object : A unique instance of a class, created based off of that blueprint (class)

# We've been working with classes and objects this entire time!!!
num = 2
print(type(num))

str1 = str() # created a string using the class constructor
print(type(str1))
str1 += 'I just contatenated this to str1'
print(str1)

list1 = list()
print(type(list1))

dictionary1 = dict()
print(type(dictionary1))

# Let's create our own class!
# Naming convention for user defined classes: Always capitalize the first letter
class Car():
    pass

# def my_func():
#     pass

d()

my_car = Car()
print(type(my_car))

bugati = Car()
my_other_car = Car()