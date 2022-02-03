

class Dog():
    """A simple attempt to model a dog"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting. ")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(self.name.title() + " is rolled over!")

my_dog = Dog('Willie' , 6)
print("My dog name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()