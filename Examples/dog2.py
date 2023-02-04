# dog2.py, Chapter 9, Python Crash Course
# program executes a dog class

class Dog():
    """a simple attempt to model a dog"""
    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name    # attribute
        self.age = age      # attribute


    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(self.title() + " rolled over!")


my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")



