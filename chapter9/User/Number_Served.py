


class Resturant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0 

    def describe_resturant(self):
        print("The resturant name is " + self.name.title())
        print("type of cuisine is " + self.type)
        print("Number of customers served is " + str(self.number_served))

    def open_resturant(self):
        """Creates the action that the resturant is open"""
        print(self.name.title() + " resturant is open")
    
    def set_number_served(self,served):
        """Sets number serves"""
        self.number_served = served
    def increment_number_served(self,serves):
        """Updates the serves the dinner has done."""
        self.number_served += serves


wes_dinner = Resturant("Wesley's dinner","bougie")
# donda=Resturant("kanye", "top notch")
# dog = Resturant("Dogs", "woof woof food")

wes_dinner.describe_resturant()
wes_dinner.open_resturant()
print("\n\n")
wes_dinner.set_number_served(3)
wes_dinner.describe_resturant()
print("\n")
wes_dinner.increment_number_served(10)
wes_dinner.describe_resturant()
# donda.describe_resturant()
# dog.describe_resturant()
