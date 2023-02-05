# exercise_09_03.py, Chapter 9, Python Crash Course
# 
# Users: Make a class called User. Create two attributes
# called first_name and last_name, and then create several
# other attributes that are typically stored in a user 
# profile. Make a method called describe_user() that prints
# a summary of the user's information. Make another method
# called greet_user() that prints a personalized greeting
# to the user.
#
# Create several instances representing different users, 
# and call both methods for each user.

class User():

    def __init__(self, first_name, last_name, team, position):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.position = position


    def describe_user(self):
        print("\nFirst name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Team: " + self.team.title())
        print("Position: " + self.position.title())


    def greet_user(self):
        print("\nWelcome to the team, " + self.first_name.title() + "!")


first_user = User('willie', 'mays', 'giants', 'center field')
first_user.describe_user()
first_user.greet_user()

second_user = User('harmon', ' killebrew', 'twins', 'left field')
second_user.describe_user()
second_user.greet_user()

third_user = User('tony', 'gwynn', 'padres', 'right field')
third_user.describe_user()
third_user.greet_user()



