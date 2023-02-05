# exercise_09_02.py, Chapter 9, Python Crash Course
# 
# Three Restaurants: Start with your class from exercise_09_01.py. 
# Create three different instances from the class, and call
# describe_restaurant() for each instance.

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant_name.title() + " has delicious " + self.cuisine_type + ".")


    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")


ted_cooks_restaurant = Restaurant('ted cooks', 'beef ribs')
ted_cooks_restaurant.describe_restaurant()

grande_sunrise_restaurant = Restaurant('grande sunrise', 'tacos')
grande_sunrise_restaurant.describe_restaurant()

sawatdee_restaurant = Restaurant('sawatdee', 'pad see yew')
sawatdee_restaurant.describe_restaurant()



