# exercise_09_01.py, Chapter 9, Python Crash Course
# 
# Restaurant: Make a class called Restaurant. The __init___()
# method for Restaurant should store two attributes: a 
# restaurant_name and a cuisine_type. Make a method called
# describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that
# prints a message indicating that the restaurant is open.

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant_name.title() + " has delicious " + self.cuisine_type + ".")


    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")


my_restaurant = Restaurant('grande sunrise', 'tacos')
print("The restaurant name is " + my_restaurant.restaurant_name.title() + ".")
print("The restaurant serves " + my_restaurant.cuisine_type + ".\n")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()



