# exercise_09_04.py, Chapter 9, Python Crash Course
# 
# Number Served: Start with your program from exercise_09_01.py.
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the
# number of customers the restaurant has served, and then change
# this value and print it again. 

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(self.restaurant_name.title() + " has delicious " + self.cuisine_type + ".")


    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")


# print the number of customers
restaurant = Restaurant('grande sunrise', 'tacos')
print("Number of customers served: " + str(restaurant.number_served))

# print the updated number of customers
restaurant.number_served = 25
print("Updated number of customers served: " + str(restaurant.number_served))


# Add a method called set_number_served() that lets you set
# the number of customers who've been served. Call this method
# with a new number and print the value again.

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(self.restaurant_name.title() + " has delicious " + self.cuisine_type + ".")


    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")


    def set_number_served(self, customers):
        """set the number of served customers"""
        self.number_served = customers

# print the updated number of customers using the set_number_served() method
restaurant = Restaurant('grande sunrise', 'tacos')
restaurant.set_number_served(40)
print("Updated number of customers served via method call: " + str(restaurant.number_served))


# Add a method called increment_number_served() that lets you
# increment the number of customers who've been served. Call
# this method with any number you like that could represent
# how many customers were served in, say, a day of business.







