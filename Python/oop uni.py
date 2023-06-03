from math import pi

class Rectangle:

    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def getArea(self):
        return self.sideA * self.sideB

    def getPerimeter(self):
        return 2 * (self.sideA + self.sideB)

class Circle(object):

    def __init__(self, r,):
        self.radius = r

    def getArea(self):
        return round(pi*(self.radius)**2)

    def getPerimeter(self):
        return round(2*pi*self.radius)

circy = Circle(11)
print(circy.getArea()) # Should return 380.132711084365
circy = Circle(4.44)
print(circy.getPerimeter()) # Should return 27.897342763877365

#2
class Calculator:

    def add(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 + self.n2

    def subtract(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 - self.n2

    def multiply(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 * self.n2

    def divide(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 / self.n2


calculator = Calculator()
print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))

#3
class Person:

    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates

    def taste(self, food_name):
        if food_name in self.likes:
            return f'{self.name} eats the {food_name} and loves it!'
        elif food_name in self.hates:
            return f'{self.name} eats the {food_name} and hates it!'
        else:
            return f'{self.name} eats the {food_name}!'


p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))
print(p1.taste("carrots"))
print(p1.taste("apple"))


#4
class OnesThreesNines:
    def __init__(self, num):
        self.__num = num

    @property
    def ones(self):
        return self.__num

    @property
    def threes(self):
        return self.__num//3

    @property
    def nines(self):
        return self.__num//9


n1 = OnesThreesNines(5)
print(n1.ones)
print(n1.nines)
print(n1.threes)

#5
class Player:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}cm"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"


p1 = Player("David Jones", 25, 175, 75)
print(p1.get_age())
print(p1.get_height())
print(p1.get_weight())


# 1
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        return f"{self.shop_name} is {self.store_type}"

    def open_shop(self):
        return f"{self.shop_name} is open"

    def set_number_of_units(self, num_of_units):
        self.number_of_units = num_of_units

    def increment_number_of_units(self):
        self.number_of_units += 1


store1 = Shop("Shopify", "online retailer")
store2 = Shop("Lidl", "grocery store")
store3 = Shop("Shein", "online fast fashion retailer")

print(store1.describe_shop())
print(store1.open_shop())

print(store2.describe_shop())
print(store3.describe_shop())

print(store1.number_of_units)


class Discount(Shop):
    pass