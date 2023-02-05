# car.py, Chapter 9, Python Crash Course
# program prints information about a car

class Car():
    """a simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())



